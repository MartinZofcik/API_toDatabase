import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.post(BASE, {"badge": "11", "fiscal_month": "2021/07",
#                          "NT_login": "aaa_aaa", "manager": "Stary Jano", "reason": "Len tak"})
# print(response.json())


response = requests.get(BASE, {"badge": "11"})
print(response.json())
