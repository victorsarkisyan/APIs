#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
api_key = sys.argv[1]
controller_ip = sys.argv[2]

url = f"https://{controller_ip}/api/v2/monitor/switch-controller/wifi/managed_ap"

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'   
}

response = requests.get(url, headers=headers, verify=False)

output = response.json()

AccessPoints = [item["name"] for item in output["results"]]
print(", ".join(AccessPoints))