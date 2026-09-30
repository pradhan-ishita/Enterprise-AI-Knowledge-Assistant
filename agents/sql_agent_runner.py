from agents.sql_agent import generate_sql
from agents.sql_validator import validate_sql
from agents.sql_answer import generate_answer
from database.sql_executor import execute_query


def run_sql_agent(question):

    # 1. Generate SQL
    sql = generate_sql(question)

    # 2. Validate SQL
    valid, message = validate_sql(sql)

    if not valid:
        return {
            "success": False,
            "sql": sql,
            "message": message,
            "answer": "I could not safely process this request."
        }

    # 3. Execute SQL
    try:
        results = execute_query(sql)

    except Exception as e:
        return {
            "success": False,
            "sql": sql,
            "message": str(e),
            "answer": "I could not retrieve the requested information."
        }

    # 4. Handle no results
    if not results:
        return {
            "success": True,
            "sql": sql,
            "results": [],
            "answer": "No matching records were found."
        }

    # 5. Generate natural-language answer
    answer = generate_answer(
        question,
        results
    )

    return {
        "success": True,
        "sql": sql,
        "results": results,
        "answer": answer
    }