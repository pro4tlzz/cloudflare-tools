import requests 
import json
import sys

from requests import api

api_key=sys.argv[1]
zone_id=sys.argv[2]

def get_list_from_file(filename):
    try:
        # open and read the file into list
        with open(filename) as f:
            string_list = f.read().splitlines()
            f.close()
            print(string_list)
            return string_list
    except:
        print("\033[1m"+"Issue Occured with obtaining list from file"+"\033[0m")
        sys.exit(1)

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
        url = "https://api.cloudflare.com/client/v4/zones/"+ zone_id +"/dns_records?type=A"

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
        #print(json.dumps(jsonContent, indent=4))
        return(jsonContent)
    except:
        print("\033[1m"+"Issue Occured with getting records"+"\033[0m")
        sys.exit(1)

def get_record_id(api_key,zone_id,records):
    try:
        for each in records:
            record_id=records["id"]
            print(record_id)
            return record_id
    except:
        print("\033[1m"+"Issue Occured with getting record IDs"+"\033[0m")
        sys.exit(1)


dns_records='records.txt'
#get_list_from_file(dns_records)
#api_success_or_fail=check_api(api_key)
remote_records=get_records(api_key,zone_id)
remote_records_ids=get_record_id(api_key,zone_id,remote_records)