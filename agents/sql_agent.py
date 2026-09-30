import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_sql(question):

    prompt = f"""
You are an SQL expert.

You are working with a MySQL database named enterprise_ai.

The database contains this table:

employees(
    employee_id INT,
    name VARCHAR(100),
    department VARCHAR(100),
    job_title VARCHAR(100),
    salary DECIMAL(10,2),
    hire_date DATE
)

Convert the user's question into a MySQL SQL query.

Rules:
1. Return ONLY the SQL query.
2. Do not use markdown code blocks.
3. Only generate SELECT queries.
4. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, or TRUNCATE.
5. Use only the employees table.
6. Do not invent columns.

User question:
{question}
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

    sql = response.choices[0].message.content.strip()

    return sql