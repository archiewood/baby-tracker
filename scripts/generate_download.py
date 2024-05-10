import os
import requests

# Read secrets from environment variables
api_key = os.getenv('API_KEY')
refresh_token = os.getenv('REFRESH_TOKEN')
uid = os.getenv('UID')
cid = os.getenv('CID')

# Auth
# Set the URL for the request
url = f"https://securetoken.googleapis.com/v1/token?key={api_key}"

# Define the request body
data = {
    "grantType": "refresh_token",
    "refreshToken": refresh_token
}

# Make the POST request
response = requests.post(url, json=data)

# Extract the access token from the response
access_token = response.json()['access_token']

# URL for the CSV export function
url = "https://us-central1-simpleintervals.cloudfunctions.net/exportCSV"

# Define the headers including the authorization token
headers = {
    "Authorization": f"Bearer {access_token}"
}
data = {
    "data": {
        "uid": uid,
        "cid": cid
    }
}

# Make the POST request to export CSV
response = requests.post(url, headers=headers, json=data)
print(response.text)