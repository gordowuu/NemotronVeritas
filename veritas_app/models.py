import streamlit as st
import json
import logging
from typing import List, Dict, Any
from dataclasses import dataclass

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings, NVIDIARerank

# Configure logging
logging.basicConfig(level=logging.INFO)

# Model Configuration
NANO_API_KEY = st.secrets["NANO_API_KEY"]
SUPER_API_KEY = st.secrets["SUPER_API_KEY"]

# Initialize our models using langchain-nvidia-ai-endpoints
ARCHITECT_MODEL = ChatNVIDIA(
    api_key=NANO_API_KEY,
    model="nvidia/nvidia-nemotron-nano-9b-v2",
    temperature=0.3,
    top_p=0.95,
    max_tokens=2048
)

RHETORIC_MODEL = ChatNVIDIA(
    api_key=SUPER_API_KEY,
    model="nvidia/llama-3.3-nemotron-super-49b-v1.5",
    temperature=0.7,
    top_p=0.95,
    max_tokens=65536
)

EMBEDDING_MODEL = NVIDIAEmbeddings(
    api_key=SUPER_API_KEY,
    model="nvidia/llama-3.2-nv-embedqa-1b-v2",
    truncate="END"
)

RERANKER_MODEL = NVIDIARerank(
    api_key=SUPER_API_KEY,
    model="nvidia/llama-3.2-nv-rerankqa-1b-v2"
)