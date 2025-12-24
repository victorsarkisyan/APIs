#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = sys.argv[1]
controller_ip = sys.argv[2]
switch = sys.argv[3]

url = f"https://{controller_ip}/api/v2/monitor/switch-controller/managed-switch/port-stats"

params = {
     'mkey': switch
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

try:
    response = requests.get(url, headers=headers, params=params, verify=False)
    response.raise_for_status()
    data = response.json()

    # flatten results list (if only one switch)
    if isinstance(data.get("results"), list) and len(data["results"]) == 1:
        data["results"] = data["results"][0]

    ports = []
    for port_name in data["results"]["ports"].keys():
        ports.append({"name": port_name})

    print(json.dumps(ports))

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)