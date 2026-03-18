from retriever import retrieve
import ollama

def reasoning_agent(query):

    chunks = retrieve(query, k=3)

    context = "\n\n".join(chunks)

    prompt = f"""
You are an enterprise AI assistant.

Use the following documents to answer the question.

Documents:
{context}

Question:
{query}

Instructions:
- Identify contradictions if they exist
- Cite relevant evidence from documents
- Explain reasoning clearly
- Provide a final conclusion
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    return answer