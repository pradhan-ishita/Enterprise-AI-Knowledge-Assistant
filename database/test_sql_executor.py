from database.sql_executor import execute_query


query = """
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3
"""


results = execute_query(query)

print("Query Results:")

for row in results:
    print(row)