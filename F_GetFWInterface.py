#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
api_key = sys.argv[1]
controller_ip = sys.argv[2]

url = f"https://{controller_ip}/api/v2/monitor/system/interface"

params = {
}

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'   
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

# Only return interface names/IDs for discovery
interfaces = []
for ifname, details in data["results"].items():
    if details["tx_bytes"] > 0 or details["rx_bytes"] > 0:
        interfaces.append({
            "{#IFNAME}": details["name"]
        })

print(json.dumps(interfaces))