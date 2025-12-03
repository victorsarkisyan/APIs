import requests
import json
import sys
import urllib3

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
api_key = sys.argv[1]
controller_ip = sys.argv[2]

url = "https://{controller_ip}/api/v2/monitor/switch-controller/managed-switch/status"

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'   
}

response = requests.get(url, headers=headers, verify=False)

output = response.json()

switch_ids = [item["switch-id"] for item in output["results"]]
print(", ".join(switch_ids))