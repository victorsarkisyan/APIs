#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = sys.argv[1]
controller_ip = sys.argv[2]
switch = sys.argv[3]

url = f"https://{controller_ip}/api/v2/monitor/switch-controller/managed-switch/port-stats"

params = {
    "mkey": switch
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(url, headers=headers, params=params, verify=False)
    response.raise_for_status()

    data = response.json()

    results = data.get("results", {})

    # flatten single-switch response
    if isinstance(results, list) and len(results) == 1:
        results = results[0]

    ports = results.get("ports", {})

    output = {
        "results": []
    }

    for port_name, stats in ports.items():

        # skip idle ports if desired
        if stats.get("tx-bytes", 0) == 0 and stats.get("rx-bytes", 0) == 0:
            continue

        output["results"].append({
            "{#PORT}": port_name,
            "tx_bytes": stats.get("tx-bytes", 0),
            "rx_bytes": stats.get("rx-bytes", 0),
            "tx_errors": stats.get("tx-errors", 0),
            "rx_errors": stats.get("rx-errors", 0),
            "tx_drops": stats.get("tx-drops", 0),
            "rx_drops": stats.get("rx-drops", 0)
        })

    print(json.dumps(output))

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)