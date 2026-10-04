import requests
token="your_access_token"
header={
    "Authorization":f"Bearer {token}"
}
response=requests.delete("http://127.0.0.1:5000/tasks/1",headers=header)
print(response.json())