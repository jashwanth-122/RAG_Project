from anthropic import Anthropic
from retrieve_chunks import retrieve_chunks
from config import CLAUDE_MODEL, TOP_K

client = Anthropic()

def generate_answer(question, top_k=TOP_K):
    results = retrieve_chunks(question, top_k=top_k)

    context_parts = []
    sources = []

    for doc, metadata in zip(results["documents"][0], results["metadatas"][0]):
        context_parts.append(f"From {metadata['source']}:\n{doc}")
        if metadata["source"] not in sources:
            sources.append(metadata["source"])

    context = "\n\n".join(context_parts)

    prompt = f"""Answer the question using only the context below. If the context doesn't contain the answer, say so.

Context:
{context}

Question: {question}

Answer:"""

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer_text = response.content[0].text

    return {
        "answer": answer_text,
        "sources": sources
    }


if __name__ == "__main__":
    questions = [
        "What model did I use for the churn prediction project, and what was the result?",
        "What was the WAPE achieved by the best model in the supply chain forecasting project?",
        "What cloud tools were used in the Olist e-commerce pipeline project?"
    ]

    for question in questions:
        result = generate_answer(question)
        print(f"Question: {question}\n")
        print(f"Answer:\n{result['answer']}")
        print(f"\nSources: {', '.join(result['sources'])}")
        print("\n" + "-" * 60 + "\n")