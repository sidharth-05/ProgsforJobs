import requests

url = "https://auth.emsicloud.com/connect/token"

payload = "client_id=uetvuc2n9d3y6c6n&client_secret=NZXCv5rY&grant_type=client_credentials&scope=emsi_open"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)