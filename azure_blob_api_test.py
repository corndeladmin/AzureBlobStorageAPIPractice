import requests

import dotenv

import os

dotenv.load_dotenv(".env")

new_container_name = input("Please enter a name for your new container: ")

sas_token = os.getenv("SAS_TOKEN")

url = f"https://todotfstateacc.blob.core.windows.net/{new_container_name}?restype=container&{sas_token}"

payload = {}
headers = {}

response = requests.request("PUT", url, headers=headers, data=payload)

print(f"Response returned with status code {response.status_code}")
