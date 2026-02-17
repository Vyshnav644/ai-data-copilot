import sqlite3
import re
from langchain_ollama import OllamaLLM


# Connect LLM
llm = OllamaLLM(model="llama3")


# Connect DB
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()


def clean_sql(query):
    query = re.sub(r"```sql", "", query)
    query = re.sub(r"```", "", query)
    return query.strip()


def ask_sql(question):

    schema = """
You are a SQL expert.

Table name: sales

Important columns:
Sales, Profit, Quantity, Order Date, Category, Sub-Category, Region, Customer Name, Product Name

Rules:
- Return ONLY SQL query
- No explanation
- No markdown
"""

    prompt = f"""
{schema}

Question:
{question}
"""

    sql_query = llm.invoke(prompt)

    sql_query = clean_sql(sql_query)

    print("\nGenerated SQL:\n", sql_query)

    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return f"Error: {e}"
