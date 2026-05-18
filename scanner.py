import requests
import random

# scan ediləcək portlar
ports = [22, 80, 443, 3306, 8080]

# random open port simulation
open_ports = [p for p in ports if random.choice([True, False])]

# göndəriləcək data
data = {
    "open_ports": open_ports
}

# BURANI SONRA DƏYİŞƏCƏYİK
url = "https://YOUR-APP.onrender.com/log"

response = requests.post(url, json=data)

print("Server response:", response.text)