from reasoning_agent import reasoning_agent
import ollama

def critic_agent(query):

    # Step 1: get reasoning answer
    reasoning_output = reasoning_agent(query)

    critic_prompt = f"""
You are a critic AI reviewing another AI's reasoning.

Question:
{query}

AI Answer:
{reasoning_output}

Your task:
1. Check if the reasoning is logically correct.
2. Identify unsupported claims.
3. Detect contradictions.
4. Suggest improvements if needed.

Return a structured evaluation.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": critic_prompt}]
    )

    critique = response["message"]["content"]

    print("\nREASONING OUTPUT:\n")
    print(reasoning_output)

    print("\nCRITIC EVALUATION:\n")
    print(critique)


query = "Are we compliant with encryption policy?"

critic_agent(query)