# Production-Level RAG System

A Retrieval-Augmented Generation (RAG) pipeline that answers questions about my own data science portfolio projects (customer churn prediction, supply chain demand forecasting, and an e-commerce data pipeline) by retrieving relevant context from project write-ups and generating grounded, cited answers with Claude.

**Live app:** https://ragproject-kbab8ngv4bbr7epdwvrjet.streamlit.app

## How it works

1. **Load documents** – reads project write-ups from the `data/` folder
2. **Chunk documents** – splits each document into overlapping ~300-word chunks
3. **Create embeddings** – converts each chunk into a vector using `sentence-transformers` (all-MiniLM-L6-v2)
4. **Store embeddings** – saves chunks and vectors in a local ChromaDB vector database
5. **Retrieve chunks** – converts a question into a vector and finds the most similar chunks
6. **Generate answer** – sends the question and retrieved chunks to Claude (Haiku) via the Anthropic API, which writes a grounded final answer with source citations

## Tools used

Python, sentence-transformers, ChromaDB, Anthropic API (Claude Haiku), Streamlit

## Evaluation

Tested with 6 questions across all three source documents. Result: 6/6 (100%) retrieval accuracy.

## Try it

A live, deployed version of this app is available here: https://ragproject-kbab8ngv4bbr7epdwvrjet.streamlit.app

You can also run it locally with `streamlit run app.py` after installing the requirements.

## Notes

This project uses an environment variable (`ANTHROPIC_API_KEY`) to keep the API key private. The key is never stored in code or committed to this repository.