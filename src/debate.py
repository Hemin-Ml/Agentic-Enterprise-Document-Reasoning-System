from reasoning import reasoning_agent
import ollama

def debate_agents(query):

    # Get reasoning output first
    reasoning_output = reasoning_agent(query)

    # -------------------------
    # Pro Agent
    # -------------------------

    pro_prompt = f"""
You are a compliance expert defending the system.

Question:
{query}

AI Reasoning:
{reasoning_output}

Your job:
Argue why the system CAN be considered compliant.
Use evidence from the reasoning if possible.
"""

    pro_response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": pro_prompt}]
    )

    pro_argument = pro_response["message"]["content"]

    # -------------------------
    # Con Agent
    # -------------------------

    con_prompt = f"""
You are a security auditor criticizing the system.

Question:
{query}

AI Reasoning:
{reasoning_output}

Your job:
Argue why the system is NOT compliant.
Identify risks and violations.
"""

    con_response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": con_prompt}]
    )

    con_argument = con_response["message"]["content"]

    print("\nREASONING OUTPUT:\n")
    print(reasoning_output)

    print("\nPRO AGENT ARGUMENT:\n")
    print(pro_argument)

    print("\nCON AGENT ARGUMENT:\n")
    print(con_argument)


query = "Are we compliant with encryption policy?"

debate_agents(query)