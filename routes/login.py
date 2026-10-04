import requests
import os
from dotenv import load_dotenv
load_dotenv()
data={
     "email":os.getenv("Email"),
    "password":os.getenv("Password")
}
response=requests.post("http://127.0.0.1:5000/users/login",json=data)
print(response.json())