# End-to-End GenAI & RAG -🎓 Machine Learning AI Assistant

## 📌 About the Project
I **developed** a Generative AI and RAG (Retrieval-Augmented Generation) system to help me in my Machine Learning and Data Science journey.

### The Problem
Every day, I watch video courses from the **Andrew Ng Machine Learning Specialization**. I copy the transcriptions and take screenshots of the slides to create PDF files for revision. 
Because I am now at the end of the specialization, I have **too many PDF files**. When I'm working on a project, it is very difficult to find exactly which file contains the answer I need.

### The Solution
I decided to build this GenAI tool as my second end-to-end project. It uses **RAG** to quickly find answers to my questions directly from Andrew Ng's video transcriptions. Instead of opening 100 PDFs, I just ask the AI.

## 🛠️ Tech Stack
*   **LlamaIndex**: The framework used for data ingestion, indexing, and query orchestration.
*   **Groq**: Powers the inference engine using Llama 3 for lightning-fast responses.
*   **HuggingFaceEmbeddings**: Used to transform text into semantic vectors (Model: all-MiniLM-L6-v2).
*   **Python**: The core language of the project.

## 🚀 Key Features
*   **Semantic Retrieval**: Understands the meaning behind questions (e.g., asking about "preventing overfitting" will find sections on Regularization).
*   **Ultra-Fast Inference**:  Integration with Groq allows for near-instantaneous responses.
*   **Contextual Accuracy**: The AI is grounded in the provided PDFs, minimizing hallucinations.
*   **End-to-End Pipeline**: From raw PDF ingestion to a chat interface.

### ⚙️ Installation
1. Clone: `git clone https://github.com/LouisPraise/GenerativeAI-RAG.git`
2. Install: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

---
🔗 **[LIVE DEMO LINK](https://generativeai-rag-my-machine-learning-ai-tutor.streamlit.app/)**
