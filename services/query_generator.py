import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_query(question):

    prompt = f"""
You are a senior SQL data analyst.

Your job is to convert natural language questions into correct SQL queries.

DATABASE SCHEMA

orders(order_id,user_id,order_number,order_dow,order_hour_of_day)

products(product_id,product_name,aisle_id,department_id)

order_products_prior(order_id,product_id,add_to_cart_order,reordered)

order_products_train(order_id,product_id,add_to_cart_order,reordered)

aisles(aisle_id,aisle)

departments(department_id,department)


TABLE RELATIONSHIPS

orders.order_id = order_products_prior.order_id

products.product_id = order_products_prior.product_id

products.aisle_id = aisles.aisle_id

products.department_id = departments.department_id


RULES

1. Always generate valid SQL.
2. Use proper JOINs when data from multiple tables is required.
3. Use aggregation functions when necessary (COUNT, SUM, AVG).
4. If the question asks for a rate or percentage, calculate it using:
   SUM(column) / COUNT(*)
5. Use GROUP BY when aggregating.
6. Use ORDER BY when ranking results.
7. Use LIMIT when asking for top results.
8. Prefer order_products_prior for historical order analysis.
9. Only generate SELECT queries (never INSERT, UPDATE, DELETE).
10. Return ONLY the SQL query without explanation.


Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        messages=[{"role": "user", "content": prompt}]
    )

    sql = response.choices[0].message.content

    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql