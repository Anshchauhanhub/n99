import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
conn_string = os.getenv("DATABASE_URL")
print(f"Connecting to: {conn_string}")

try:
    conn = psycopg.connect(conn_string)
    print("Success!")
    conn.close()
except Exception as e:
    print(f"Failure: {e}")
