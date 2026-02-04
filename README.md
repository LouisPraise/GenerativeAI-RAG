# 🎓 AI Tutor: RAG System for Andrew Ng’s ML Specialization

## 📌 Project Overview
As I progress through the **Andrew Ng Machine Learning Specialization**, I’ve built a massive library of personalized study materials, including video transcriptions and slide screenshots compiled into numerous PDF files. 

**The Problem:** With dozens of files, finding a specific technical explanation (like "backpropagation logic" or "bias-variance tradeoff") during a project became a time-consuming manual task.

**The Solution:** I'm developing an end-to-end **RAG (Retrieval-Augmented Generation)** pipeline. This assistant will allow me to query my entire collection of course notes using natural language, providing instant, context-aware answers directly from Andrew Ng's teachings.

## 🛠️ Tech Stack
*   **Orchestration:** [LlamaIndex](https://www.llamaindex.ai) (Optimized for data retrieval)
*   **LLM Provider:** [Groq](https://groq.com) (Chosen for ultra-fast inference speeds)
*   **Embeddings:** [HuggingFace](https://huggingface.co) (Local open-source embeddings)
*   

## 🚀 Key Features
- **Semantic Search:** Understands the meaning of my questions, not just keywords.
- **Source Attribution:** The assistant points to the specific PDF and page used to generate the answer.
- **Zero-Latency:** Integrated with **Groq** to ensure near-instant feedback during study sessions.

