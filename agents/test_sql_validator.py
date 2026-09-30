from agents.sql_validator import validate_sql


# Safe query
safe_query = """
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
"""

valid, message = validate_sql(safe_query)

print("Safe Query:")
print("Valid:", valid)
print("Message:", message)


# Dangerous query
dangerous_query = """
DROP TABLE employees;
"""

valid, message = validate_sql(dangerous_query)

print("\nDangerous Query:")
print("Valid:", valid)
print("Message:", message)