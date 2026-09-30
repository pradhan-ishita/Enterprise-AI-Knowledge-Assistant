import os
from decimal import Decimal

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, results):

    # Format database results
    formatted_results = []

    for row in results:

        formatted_row = {}

        for key, value in row.items():

            if isinstance(value, Decimal):

                # Remove unnecessary decimal places
                if value == value.to_integral_value():
                    value = f"{int(value):,}"
                else:
                    value = f"{value:,.2f}"

            formatted_row[key] = value

        formatted_results.append(formatted_row)


    prompt = f"""
You are an enterprise AI assistant.

Answer the user's question using ONLY the database results provided below.

User question:
{question}

Database results:
{formatted_results}

Rules:

1. Give a clear and concise natural-language answer.
2. Do not invent information.
3. Do not mention SQL, databases, Python, or internal system details.
4. If there are multiple results, present them clearly.
5. Do NOT assume or add a currency symbol unless the database results explicitly provide a currency.
6. Preserve the numerical values exactly as provided.
7. Use comma separators for large numbers when appropriate.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()