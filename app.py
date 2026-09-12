import sys
import os

# make sure Python can find the scripts inside src
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
from generate_answer import generate_answer

st.set_page_config(page_title="Ask My Projects", page_icon=":mag:")

st.title("Ask my project documents")
st.write("A RAG system that answers questions about my data science portfolio projects, grounded in my own project write-ups.")

question = st.text_input("Ask a question about my churn, supply chain, or e-commerce projects:")

if st.button("Ask") and question:
    with st.spinner("Searching documents and generating answer..."):
        result = generate_answer(question)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")
    for source in result["sources"]:
        st.write(f"- {source}")