import requests
import time

# URL of the endpoint
num = 'a'
url_bake = "https://cookie.dicec.tf/bake?number={}".format(num)

# URL
url_deliver = "https://cookie.dicec.tf/deliver"

# HTTP headers
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "content-length": "0",
    "dnt": "1",
    "origin": "https://cookie.dicec.tf",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://cookie.dicec.tf/",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}

# Cookies required for session authentication
user = "34jx33ezjk5" # original

cookies = {
    "user": user
}

response = requests.post(url_bake, headers=headers, cookies=cookies)
print(f"Status {response.status_code} - Response: {response.text}")


# Send POST request
response = requests.post(url_deliver, headers=headers, cookies=cookies)

# Print response status and content
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
