import streamlit as st
from analyzer import VeritasAnalyzer

st.set_page_config(
    page_title="Nemotron Veritas - Misinformation Analysis",
    page_icon="🔍",
    layout="wide"
)

# Initialize the analyzer
@st.cache_resource
def get_analyzer():
    return VeritasAnalyzer()

analyzer = get_analyzer()

# Title and description
st.title("🔍 Nemotron Veritas")
st.subheader("AI-Powered Misinformation Analysis")

st.markdown("""
This tool analyzes text to identify rhetorical devices, logical fallacies, and persuasive techniques.
It uses NVIDIA's advanced language models to provide a comprehensive analysis of argumentative structures.

**How it works:**
1. Enter your text in the box below
2. The system will identify the main thesis and supporting claims
3. Each claim will be analyzed for logical fallacies
4. A comprehensive analysis report will be generated
""")

# Input text area
text_input = st.text_area(
    "Enter text to analyze:",
    height=200,
    placeholder="Paste your text here...",
    help="Enter the text you want to analyze for rhetorical devices and logical fallacies."
)

# Analysis button
if st.button("Analyze Text", type="primary"):
    if not text_input:
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing text..."):
            try:
                # Run analysis
                report = analyzer.analyze_text(text_input)
                
                # Display results in expandable sections
                with st.expander("Main Thesis", expanded=True):
                    st.markdown(f"**{report.thesis}**")
                
                with st.expander("Claims Analysis", expanded=True):
                    for analysis in report.claims_analysis:
                        st.markdown("---")
                        st.markdown(f"**Claim:** {analysis.claim}")
                        if analysis.detected_fallacies:
                            st.markdown("**Detected Fallacies:**")
                            for fallacy in analysis.detected_fallacies:
                                st.markdown(f"- {fallacy['name']}")
                        else:
                            st.markdown("**No logical fallacies detected**")
                        st.markdown(f"**Analysis:** {analysis.explanation}")
                
                with st.expander("Summary Analysis", expanded=True):
                    st.markdown(report.summary)
                    
            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
Made with ❤️ using NVIDIA's Nemotron models:
- Architect: nvidia-nemotron-nano-9b-v2
- Rhetoric: llama-3.3-nemotron-super-49b-v1.5
- Embeddings: llama-3.2-nv-embedqa-1b-v2
""")