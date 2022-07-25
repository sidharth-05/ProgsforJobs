import requests

url = "https://emsiservices.com/skills/versions/latest/skills"

querystring = {"typeIds":"ST1,ST2","fields":"id,name,type,infoUrl"}

payload = "{ \"ids\": [ \"KS1200364C9C1LK3V5Q1\", \"KS1275N74XZ574T7N47D\", \"KS125QD6K0QLLKCTPJQ0\" ] }"
headers = {
    'Authorization': "Bearer ",
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)