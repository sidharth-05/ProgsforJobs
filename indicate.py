import requests


url = "https://emsiservices.com/skills/status"
url_skills = "https://emsiservices.com/skills/versions/latest/skills?q=.NET&typeIds=ST1%2CST2&fields=id%2Cname%2Ctype%2CinfoUrl&limit=5"


headers = {'Authorization': 'Bearer '}

response = requests.request("GET", url_skills, headers=headers)

print(response.text)