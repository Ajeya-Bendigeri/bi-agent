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
You are an SQL expert.

Database schema:    

orders(order_id,user_id,order_number,order_dow,order_hour_of_day)
products(product_id,product_name,aisle_id,department_id)
order_products_prior(order_id,product_id,add_to_cart_order,reordered)
order_products_train(order_id,product_id,add_to_cart_order,reordered)
aisles(aisle_id,aisle)
departments(department_id,department)

Return ONLY SQL.

Question: {question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    sql = response.choices[0].message.content

    # remove markdown formatting
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql



#without API_key

# def generate_query(question):

#     q = question.lower()

#     if "top products" in q or "most ordered products" in q:
#         return """
#         SELECT product_id, COUNT(*) AS total_orders
#         FROM order_products_prior
#         GROUP BY product_id
#         ORDER BY total_orders DESC
#         LIMIT 10
#         """

#     elif "total orders" in q:
#         return """
#         SELECT COUNT(*) AS total_orders
#         FROM orders
#         """

#     elif "products" in q:
#         return """
#         SELECT *
#         FROM products
#         LIMIT 10
#         """

#     elif "departments" in q:
#         return """
#         SELECT *
#         FROM departments
#         """

#     elif "aisles" in q:
#         return """
#         SELECT *
#         FROM aisles
#         """

#     else:
#         return """
#         SELECT *
#         FROM products
#         LIMIT 5
#         """