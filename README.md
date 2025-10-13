# Nemotron Veritas

A sophisticated multi-agent system designed to act as a "critical thinking amplifier" using NVIDIA's Nemotron family of models. The system analyzes text to reveal rhetorical devices, logical fallacies, and persuasive techniques.

## System Architecture

1. **Architect Agent** (nvidia-nemotron-nano-9b-v2)
   - Analyzes text structure
   - Extracts main thesis and supporting claims

2. **Rhetoric Agent** (llama-3_3-nemotron-super-49b-v1_5)
   - Examines claims for logical fallacies
   - Uses RAG pipeline with fallacies knowledge base

3. **Synthesizer Agent** (nvidia-nemotron-nano-9b-v2)
   - Combines analyses
   - Formats structured output

## Tech Stack

- **AI Models & APIs**
  - NVIDIA Nemotron Models
  - LangChain for orchestration
  - FAISS for vector storage
  - Sentence Transformers for embeddings

## Setup

1. Install dependencies:
```bash
pip install -q langchain langchain-community faiss-cpu openai python-dotenv tqdm sentence-transformers langchain-nvidia-ai-endpoints
```

2. Configure environment variables:
Create a `.env` file with your NVIDIA API keys:
```
NANO_API_KEY=your_nano_api_key
SUPER_API_KEY=your_super_api_key
```

3. Run the Jupyter notebook:
```bash
jupyter notebook Veritas_Agent_Notebook.ipynb
```

## Features

- Text structure analysis
- Logical fallacy detection
- Rhetorical device identification
- Comprehensive report generation
- RAG-based knowledge retrieval

## Test Cases

The system includes a comprehensive test suite with various cases:
1. Emotional Appeal + Fear Mongering
2. False Authority + Cherry Picking
3. Conspiracy Theory Structure
4. False Dichotomy + Slippery Slope
5. Appeal to Nature + False Causation