import requests

url = "http://localhost:8585/predict"

input = {}

response = requests.post(url,json=input).json()

print(response)