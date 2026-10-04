import requests
token="your_access_token"
header={
    "Authorization":f"Bearer {token}"
}
response=requests.get("http://127.0.0.1:5000/tasks",headers=header)
print(response.json())