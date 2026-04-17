#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = sys.argv[1]
controller_ip = sys.argv[2]

url = f"https://{controller_ip}/api/v2/monitor/wifi/managed_ap"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

results = data.get("results", [])

for ap in results:
    print(f"{ap.get('name')}, {ap.get('serial')}")