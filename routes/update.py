import requests
data={
    "status":"Completed"
}
token="your_access_token"
header={
    "Authorization":f"Bearer {token}"
}
response=requests.put("http://127.0.0.1:5000/tasks/1",json=data,headers=header) 
print(response.json())