#!/usr/bin/env python3

import requests
import json
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = sys.argv[1]
controller_ip = sys.argv[2]
ap_id = sys.argv[3]

url = f"https://{controller_ip}/api/v2/monitor/wifi/managed_ap"
params = {"wtp_id": ap_id}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers, params=params, verify=False)

data = response.json()
results = data.get("results", [])

output = {
    "results": []
}

for ap in results:
    ap_entry = {
        "name": ap.get("name"),
        "radio": []
    }

    for radio in ap.get("radio", []):
        # skip invalid radios
        if radio.get("radio_type", "").lower() == "unknown":
            continue

        ap_entry["radio"].append({
            "radio_id": radio.get("radio_id"),
            "tx_bytes": radio.get("bytes_tx", 0),
            "bytes_rx": radio.get("bytes_rx", 0),
            "tx_power": radio.get("oper_txpower", 0),
            "client_count": radio.get("client_count", 0)
        })

    output["results"].append(ap_entry)

print(json.dumps(output))