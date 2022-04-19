import requests
import json
import pprint

from random_ip_generator import generate_ip_addresses



api_url = ''
api_targets = []
headers = {}


for api_target in api_targets:
    url = api_url + api_target
    ip_addresses = generate_ip_addresses(1)
    
    for ip_address in ip_addresses:
        params = {'ip': ip_address}
        response = requests.get(url=url, headers=headers, params=params)
        if response.status_code == 200:
            jsonified_response = json.loads(response.text)
            json_formatted_str = json.dumps(jsonified_response, indent=2)
            print(json_formatted_str)
