import requests
import random

ports = [22, 80, 443, 3306, 8080]
open_ports = [p for p in ports if random.choice([True, False])]

data = {"open_ports": open_ports}

headers = {
    "x-api-key": "SECURE123"
}

url = "https://securitytool-6tc6.onrender.com/log"

response = requests.post(url, json=data, headers=headers)

print("Response:", response.text)