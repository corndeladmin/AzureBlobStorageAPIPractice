import requests

import dotenv

import os

dotenv.load_dotenv(".env")

container_name = "alextestcontainer"

file_name = "NASA.png"

image_file = open("DockerDiagram.png", "rb")

image_content = image_file.read()

nasa_response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

response_dict = nasa_response.json()

image_url = response_dict["url"]

nasa_image_response = requests.get(image_url)

contents = nasa_image_response.content

sas_token = os.getenv("SAS_TOKEN")

url = f"https://todotfstateacc.blob.core.windows.net/{container_name}/{file_name}?{sas_token}"

headers = {
    "x-ms-blob-type": "BlockBlob"
}

response = requests.request("PUT", url, data=contents, headers=headers)

print(response.text)

print(f"Response returned with status code {response.status_code}")

response.raise_for_status()