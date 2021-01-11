
"""
Purpose: StackOverflow question on APIs
Date created: 2020-05-17

URL: https://stackoverflow.com/questions/61859748/i-am-trying-to-get-the-access-token-for-my-worker-application-but-i-get-the-req/61860072#61860072

Contributor(s):
    Mark M.
"""


import requests

# Initial setup
paths = ["api.pingone.com", "api.pingone.eu", "api.pingone.asia"]
apiPath = 'api.pingone.com/v1/environments'
apiPath = 'api.pingone.com/v1/environments'

envID = '5bb98115-61c7-4964-96bf-4d2c3a34756b'
appID = 'db04865b-9ab0-448e-a89a-f3cb473ddc7f'
appSecret = 'c_5XTOw6Sh-ei6cHLhvoneoVn-86t.zY1Df7YWcIUfpkN4gTjp1A7QjWUwlEpofp'

url = f"https://{apiPath}/{envID}/as/token"

payload = 'grant_type=client_credentials'
headers = {
   'Content-Type': 'application/x-www-form-urlencoded',
   'Authorization': f'Basic {appID}:{appSecret}'
}


response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))







# Get
paths = ["auth.pingone.com", "auth.pingone.eu", "auth.pingone.asia"]
authPath = f'https://{paths[0]}'
envID = '5bb98115-61c7-4964-96bf-4d2c3a34756b'
appID = 'db04865b-9ab0-448e-a89a-f3cb473ddc7f'

url = f"{authPath}/{envID}/as/authorize?response_type=code&client_id={appID}&redirect_uri=https://example.com&scope=openid profile p1:read:user"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

res = response.text.encode('utf8')
print(res)



# Post
paths = ["auth.pingone.com", "auth.pingone.eu", "auth.pingone.asia"]

authPath = f'https://auth.pingone.com'
envID = '5bb98115-61c7-4964-96bf-4d2c3a34756b'
appID = 'db04865b-9ab0-448e-a89a-f3cb473ddc7f'
url = f"{authPath}/{envID}/as/authorize"

payload = {
        "response_type":"code",
        "client_id":f"{appID}",
        "redirect_uri":"https://example.com",
        "scope":"openid profile p1:read:user",
    }

# payload = 'response_type=code&client_id={appID}&redirect_uri=https://example.com&scope=openid profile p1:read:user'


headers = {
   'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST",
                            url,
                            headers = headers,
                            data = payload
                            )
response.status_code

print(response.text.encode('utf8'))
print(response.text)








