import requests
import os
from dotenv import load_dotenv
load_dotenv()
data={
    "username":os.getenv("User_name"),
    "email":os.getenv("Email"),
    "password":os.getenv("Password")
    
}
response=requests.post("http://127.0.0.1:5000/users/register",json=data)
print(response.json())