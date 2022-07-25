import requests

url = "https://emsiservices.com/skills/versions/latest/skills"

querystring = {"typeIds":"ST1,ST2","fields":"id,name,type,infoUrl"}

payload = "{ \"ids\": [ \"KS1200364C9C1LK3V5Q1\", \"KS1275N74XZ574T7N47D\", \"KS125QD6K0QLLKCTPJQ0\" ] }"
headers = {
    'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNDNjZCRjIzMjBGNkY4RDQ2QzJERDhCMjI0MEVGMTFENTZEQkY3MUYiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJQR2FfSXlEMi1OUnNMZGl5SkE3eEhWYmI5eDgifQ.eyJuYmYiOjE2NTg3ODc4NjksImV4cCI6MTY1ODc5MTQ2OSwiaXNzIjoiaHR0cHM6Ly9hdXRoLmVtc2ljbG91ZC5jb20iLCJhdWQiOlsiZW1zaV9vcGVuIiwiaHR0cHM6Ly9hdXRoLmVtc2ljbG91ZC5jb20vcmVzb3VyY2VzIl0sImNsaWVudF9pZCI6InVldHZ1YzJuOWQzeTZjNm4iLCJlbWFpbCI6InNpZGhhcnRoLm1hbGxlbGFAZ21haWwuY29tIiwiY29tcGFueSI6IlNlbGYtZW1wbG95ZWQiLCJuYW1lIjoiU2lkaGFydGggTWFsbGVsYSIsImlhdCI6MTY1ODc4Nzg2OSwic2NvcGUiOlsiZW1zaV9vcGVuIl19.r_si2H4r9cYqJaD2VSvuhlJ4DPP4-sLNvO-CwHap1cAT_Z1SK2PmPHwRgxARbEqqD1ofs_NdaEoRlhEeZZFVtURxAzpKvSugYnV7_OktxysRSfNyCGaSVOYa-6CjOeakH1m6B3TFlw7qYmFIx6LSiBXviLnEf5VxhzRV-Lqof0Z2yGdwIQeILsfHbSWqywVxtOv2gr6f-zcpUMCKwFWUgnT14qHOFdgKFNxbin7NUMxhHPSC11f5YxF6mkCKvJiHueWRxTYSlezIDEB0zyP5dPXLdfNHTTyXW1AvOuwI6ImNucQpBDp_QdXdElMpbBmnPetMhIVZH1Xw8oty7STIcA",
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)