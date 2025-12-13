#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
# api_key = 
# controller_ip = ""

url = f"https://192.168.0.1/api/v2/monitor/switch-controller/managed-switch/status"

params = {
  'mkey': 'Switch_Office',
}

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer bg5NjG4N4pst0zkwQpm9kcdqjHsz5p'   
}

response = requests.get(url, headers=headers, params=params, verify=False)

output = response.json()
print(output)
# switch_ids = [item["switch-id"] for item in output["results"]]
# print(", ".join(switch_ids))