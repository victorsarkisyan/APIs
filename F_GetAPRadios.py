#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

# Disable insecure warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Arguments from Zabbix
api_key = sys.argv[1]
controller_ip = sys.argv[2]
ap_id = sys.argv[3]

url = f"https://{controller_ip}/api/v2/monitor/wifi/managed_ap"
params = {"wtp_id": ap_id}
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers, params=params, verify=False)
results = response.json().get("results", [])

lld_data = {"data": []}

for radio in results[0].get('radio', []):
    # Skip radios with unknown type
    if radio.get("radio_type") and radio["radio_type"].lower() != "unknown":
        lld_data["data"].append({
            "{#RADIOID}": radio["radio_id"],
            "{#RADIOTYPE}": radio["radio_type"]
        })

print(json.dumps(lld_data))