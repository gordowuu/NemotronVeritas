# Nemotron Veritas

A sophisticated multi-agent system designed to act as a "critical thinking amplifier" using NVIDIA's Nemotron family of models. The system analyzes text to reveal rhetorical devices, logical fallacies, and persuasive techniques.

## 🚀 Live Demo

**Try it now:** [https://nemotronveritas.streamlit.app/](https://nemotronveritas.streamlit.app/)

## System Architecture

The system uses a three-agent architecture powered by NVIDIA's Nemotron models:

1. **Architect Agent** (nvidia-nemotron-nano-9b-v2)
   - Analyzes text structure and identifies the main thesis
   - Extracts key supporting claims from the argument
   - Temperature: 0.3 for precise, deterministic analysis

2. **Rhetoric Agent** (llama-3_3-nemotron-super-49b-v1_5)
   - Examines each claim for logical fallacies
   - Uses RAG (Retrieval Augmented Generation) pipeline with fallacies knowledge base
   - Leverages FAISS vector database for similarity search
   - Temperature: 0.7 for nuanced rhetorical analysis

3. **Synthesizer Agent** (nvidia-nemotron-nano-9b-v2)
   - Combines analyses from both agents
   - Generates comprehensive, structured reports
   - Identifies overall persuasive patterns and strategies

## Tech Stack

### AI Models & Endpoints
- **nvidia-nemotron-nano-9b-v2** - Text structure analysis and report synthesis
- **llama-3.3-nemotron-super-49b-v1.5** - Rhetorical analysis with 65K token context
- **llama-3.2-nv-embedqa-1b-v2** - Text embeddings for semantic search
- **llama-3.2-nv-rerankqa-1b-v2** - Result reranking for improved accuracy

### Framework & Libraries
- **LangChain** - AI agent orchestration and chaining
- **FAISS** - High-performance vector similarity search
- **Streamlit** - Interactive web interface
- **Sentence Transformers** - Text embedding generation
- **Python 3.9+** - Core runtime environment

## Installation & Setup

### Option 1: Run Locally

1. Clone the repository:
```bash
git clone https://github.com/gordowuu/NemotronVeritas.git
cd NemotronVeritas
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file with your NVIDIA API keys:
```env
NANO_API_KEY=your_nano_api_key_here
SUPER_API_KEY=your_super_api_key_here
```

4. Run the Streamlit app:
```bash
cd veritas_app
streamlit run app.py
```

### Option 2: Use Jupyter Notebook

1. Open the notebook:
```bash
jupyter notebook Veritas_Agent_Notebook.ipynb
```

2. Run all cells sequentially to initialize the system

3. Use the test suite or create your own analysis

## Features

- **Real-time Analysis** - Instant detection of rhetorical manipulation
- **Multi-Agent System** - Three specialized AI agents working in concert
- **RAG Pipeline** - Knowledge-enhanced fallacy detection
- **Interactive UI** - User-friendly Streamlit interface
- **Comprehensive Reports** - Detailed breakdown of claims and fallacies
- **Extensible Database** - Easily add new fallacy patterns

## Test Cases

The system includes a comprehensive test suite with various misinformation scenarios:

1. **Emotional Appeal + Fear Mongering** - Climate change denial rhetoric
2. **False Authority + Cherry Picking** - Health misinformation tactics
3. **Conspiracy Theory Structure** - Political manipulation patterns
4. **False Dichotomy + Slippery Slope** - Education policy framing
5. **Appeal to Nature + False Causation** - Health product marketing

## How It Works

1. **Input**: User submits text for analysis
2. **Structure Analysis**: Architect agent identifies thesis and claims
3. **Fallacy Detection**: Rhetoric agent searches for logical fallacies using RAG
4. **Synthesis**: Synthesizer agent creates comprehensive report
5. **Output**: Detailed analysis with identified fallacies and explanations

## API Keys

To run locally, you'll need NVIDIA API keys:
- Get them at: [https://build.nvidia.com/](https://build.nvidia.com/)
- Required models: Nemotron Nano 9B v2, Llama 3.3 Nemotron Super 49B v1.5

## Project Structure

```
NemotronVeritas/
├── veritas_app/           # Streamlit application
│   ├── app.py            # Main Streamlit UI
│   ├── analyzer.py       # Core analysis logic
│   ├── models.py         # Model configurations
│   └── requirements.txt  # App dependencies
├── Veritas_Agent_Notebook.ipynb  # Jupyter notebook version
├── .streamlit/           # Streamlit configuration
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Contributing

Contributions are welcome! Areas for improvement:
- Expand the fallacy database
- Add more test cases
- Improve UI/UX
- Optimize model performance
- Add multi-language support

## License

MIT License - feel free to use and modify

## Acknowledgments

- Built with NVIDIA's Nemotron AI models
- Powered by LangChain framework
- Deployed on Streamlit Cloud

---

**Live Demo**: [https://nemotronveritas.streamlit.app/](https://nemotronveritas.streamlit.app/)