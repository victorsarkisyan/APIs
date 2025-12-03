#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
api_key = sys.argv[1]
controller_ip = sys.argv[2]
ap_id = sys.argv[3]

url = f"https://{controller_ip}/api/v2/monitor/wifi/managed_ap"

params = {
    "wtp_id": ap_id
}

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'   
}

response = requests.get(url, headers=headers, params=params,  verify=False)

output = response.json()

results = output.get("results", [])
print(results[0]['serial'])