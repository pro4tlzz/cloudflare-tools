import requests 
import json
import sys

from requests import api

api_key=sys.argv[1]
zone_id=sys.argv[2]

def check_api(api_key):
    try:
        url = "https://api.cloudflare.com/client/v4/user/tokens/verify"

        headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization": "Bearer " + api_key
        }

        response = requests.request(
        "GET",
        url,
        headers=headers,
        )

        jsonContent = json.loads(response.text)
        print(jsonContent)
    except:
        print("\033[1m"+"Issue Occured with checking API"+"\033[0m")
        sys.exit(1)

def get_records(api_key,zone_id):
    try:
        url = "https://api.cloudflare.com/client/v4/zones/"+ zone_id +"/dns_records"

        headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization": "Bearer " + api_key
        }

        response = requests.request(
        "GET",
        url,
        headers=headers,
        )

        jsonContent = json.loads(response.text)
        print(jsonContent)
    except:
        print("\033[1m"+"Issue Occured with getting records"+"\033[0m")
        sys.exit(1)
		
api_success_or_fail=check_api(api_key)
remote_records=get_records(api_key,zone_id)