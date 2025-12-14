#!/usr/bin/env python3

import subprocess
import json
import sys

api_key = sys.argv[1]
controller_ip = sys.argv[2]
site_id = sys.argv[3]
device_id = sys.argv[4]

url = f"https://{controller_ip}/proxy/network/integration/v1/sites/{site_id}/devices/{device_id}/statistics/latest"

curl_command = [
    "curl",
    "-k",                     # <-- allow self-signed SSL certs
    "-X", "GET",
    "-H", f"x-api-key: {api_key}",
    "-H", "Content-Type: application/json",
    url
]

result = subprocess.run(curl_command, capture_output=True, text=True)

data =json.loads(result.stdout)
print(data.get("loadAverage1Min"))
