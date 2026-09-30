import re


def validate_sql(query):

    query = query.strip()

    # Must start with SELECT
    if not query.upper().startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    # Dangerous SQL keywords
    forbidden_keywords = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "TRUNCATE",
        "CREATE",
        "GRANT",
        "REVOKE"
    ]

    query_upper = query.upper()

    for keyword in forbidden_keywords:

        if re.search(r"\b" + keyword + r"\b", query_upper):
            return False, f"Forbidden SQL keyword detected: {keyword}"

    return True, "SQL query is valid."