from agents.sql_agent import generate_sql
from agents.sql_validator import validate_sql
from database.sql_executor import execute_query


question = "Who are the top 3 highest-paid employees?"

# Step 1: Generate SQL
sql = generate_sql(question)

print("Generated SQL:")
print(sql)


# Step 2: Validate SQL
valid, message = validate_sql(sql)

print("\nSQL Validation:")
print("Valid:", valid)
print("Message:", message)


# Step 3: Execute only if valid
if valid:

    results = execute_query(sql)

    print("\nQuery Results:")

    for row in results:
        print(row)

else:

    print("\nQuery was blocked for security reasons.")