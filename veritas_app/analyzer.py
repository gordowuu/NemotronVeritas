from dataclasses import dataclass
from typing import List, Dict, Any
import json
import logging

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from models import (
    ARCHITECT_MODEL,
    RHETORIC_MODEL,
    EMBEDDING_MODEL,
)

# Data structures
@dataclass
class TextStructure:
    thesis: str
    claims: List[str]

@dataclass
class FallacyAnalysis:
    claim: str
    detected_fallacies: List[Dict[str, Any]]
    explanation: str

@dataclass
class AnalysisReport:
    text: str
    thesis: str
    claims_analysis: List[FallacyAnalysis]
    summary: str

# Fallacies database
LOGICAL_FALLACIES = [
    {
        "name": "Ad Hominem",
        "description": "Attacking the person instead of addressing their argument",
        "example": "You can't trust his economic policy because he's never had a real job."
    },
    {
        "name": "Straw Man",
        "description": "Misrepresenting someone's argument to make it easier to attack",
        "example": "Environmentalists want us to go back to living in caves without electricity."
    },
]

class VeritasAnalyzer:
    def __init__(self):
        # Create documents from fallacies
        documents = []
        for fallacy in LOGICAL_FALLACIES:
            text = f"Fallacy: {fallacy['name']}\nDescription: {fallacy['description']}\nExample: {fallacy['example']}"
            documents.append(Document(page_content=text, metadata=fallacy))

        # Create FAISS vector store with embeddings
        self.vectordb = FAISS.from_documents(documents, EMBEDDING_MODEL)

        # Create a simple similarity search retriever
        self.fallacy_retriever = self.vectordb.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )

    def analyze_structure(self, text: str) -> TextStructure:
        """Analyze text structure to identify thesis and claims."""
        prompt = """
        Analyze the following text and identify:
        1. The main thesis (central argument)
        2. The key supporting claims
        
        Text: {text}
        
        Output your analysis in JSON format with 'thesis' and 'claims' fields.
        """
        messages = [{"role": "system", "content": prompt.format(text=text)}]
        response = ARCHITECT_MODEL.invoke(messages).content
        
        try:
            result = json.loads(response)
            return TextStructure(
                thesis=result['thesis'],
                claims=result['claims']
            )
        except Exception as e:
            logging.error(f"Error parsing Architect response: {e}")
            raise

    def analyze_claim(self, claim: str) -> FallacyAnalysis:
        """Analyze a claim for logical fallacies."""
        # Get relevant fallacy patterns with reranking
        docs = self.fallacy_retriever.invoke(claim)
        context = "\n\n".join(doc.page_content for doc in docs)
        
        prompt = """You are a logical fallacy detection system. Analyze the following claim:

Claim: {claim}

Relevant fallacy patterns:
{context}

Output your findings in JSON format:
{{
    "detected_fallacies": [
        {{"name": "Fallacy Name", "type": "Type of Fallacy"}}
    ],
    "explanation": "Detailed explanation of how these fallacies are used"
}}
"""
        messages = [{"role": "system", "content": prompt.format(claim=claim, context=context)}]
        response = RHETORIC_MODEL.invoke(messages).content.strip()
        
        try:
            if not response.startswith('{'):
                start_idx = response.find('{')
                if start_idx != -1:
                    response = response[start_idx:]
                    end_idx = response.rfind('}')
                    if end_idx != -1:
                        response = response[:end_idx + 1]
            
            result = json.loads(response)
            if "detected_fallacies" not in result or "explanation" not in result:
                result = {
                    "detected_fallacies": [],
                    "explanation": "Failed to detect fallacies in a structured way."
                }
            
            return FallacyAnalysis(
                claim=claim,
                detected_fallacies=result['detected_fallacies'],
                explanation=result['explanation']
            )
        except Exception as e:
            logging.error(f"Error parsing Rhetoric response: {e}")
            return FallacyAnalysis(
                claim=claim,
                detected_fallacies=[],
                explanation="Failed to analyze this claim due to processing error."
            )

    def create_report(self, text: str, structure: TextStructure, claims_analysis: List[FallacyAnalysis]) -> str:
        """Create a summary report of the analysis."""
        claims_str = "\n\n".join(
            f"Claim: {analysis.claim}\n"
            f"Fallacies: {', '.join(f['name'] for f in analysis.detected_fallacies)}\n"
            f"Explanation: {analysis.explanation}"
            for analysis in claims_analysis
        )
        
        prompt = """Create a comprehensive summary of the rhetorical analysis:
        
        Original Text: {text}
        Main Thesis: {thesis}
        Claims Analysis: {claims_analysis}
        
        Focus on patterns and overall persuasive strategy.
        """
        messages = [{"role": "system", "content": prompt.format(
            text=text,
            thesis=structure.thesis,
            claims_analysis=claims_str
        )}]
        return ARCHITECT_MODEL.invoke(messages).content

    def analyze_text(self, text: str) -> AnalysisReport:
        """Main analysis pipeline."""
        try:
            # Step 1: Extract structure
            logging.info("Analyzing text structure...")
            structure = self.analyze_structure(text)
            
            # Step 2: Analyze each claim
            logging.info("Analyzing claims for fallacies...")
            claims_analysis = []
            for claim in structure.claims:
                analysis = self.analyze_claim(claim)
                claims_analysis.append(analysis)
            
            # Step 3: Generate final report
            logging.info("Generating final report...")
            summary = self.create_report(text, structure, claims_analysis)
            
            return AnalysisReport(
                text=text,
                thesis=structure.thesis,
                claims_analysis=claims_analysis,
                summary=summary
            )
            
        except Exception as e:
            logging.error(f"Error in analysis pipeline: {e}")
            raise