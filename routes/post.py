import requests
data={
    "title":"Creating Task_Management API",
    "description":"creating API and stores tasks in Mysql",
    "status":"Pending"
}
token="your_access_token"
header={
    'Authorization':f"Bearer {token}"
}
response=requests.post("http://127.0.0.1:5000/tasks",json=data,headers=header)
print(response.json())