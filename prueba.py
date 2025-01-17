# Dependencies to install:
# $ python -m pip install requests
import requests

CLIENT_ID = 'TjlQbIGfxQYCpCUv1oTEz6PmiDQC0Jpf'
CLIENT_SECRET = '17RtoLfz7FQRsVfdfv5fRj1StW3YPzA6EU82QewtXr7XXE9PD5uds0mi549iqsUn'

API_URL = 'https://api.getport.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}

token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)

access_token = token_response.json()['accessToken']

# You can now use the value in access_token when making further requests

headers = {
	'Authorization': f'Bearer {access_token}'
}

blueprint_id = 'service'

entity = {
  "identifier": "some_identifier",
  "title": "Some Title",
  "properties": {
    "readme": "string",
    "url": "https://example.com",
    "language": "string",
    "slack": "https://example.com",
    "tier": "Mission Critical"
  },
  "relations": {}
}

response = requests.post(f'{API_URL}/blueprints/{blueprint_id}/entities?upsert=true', json=entity, headers=headers)

# response.json() contains the content of the resulting entity