import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
conn=mysql.connector.connect(
    host=os.getenv("db_host"),
    user=os.getenv("db_user"),
    password=os.getenv("db_password"),
    database=os.getenv("db_database")
)
cursor=conn.cursor()
print("Successfully connected to my sql ")
