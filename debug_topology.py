import requests
import json

try:
    response = requests.get('http://127.0.0.1:8000/api/simulation/topology')
    data = response.json()
    print(json.dumps(data, indent=2))
except Exception as e:
    print(e)
