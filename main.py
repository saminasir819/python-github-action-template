import requests

discord_webhook_url = ""

payload = {
    "content": "NIHAOOOOOOOOOOOOOOOOOOOOOO",
    "username": "Test Bot"
}

response = requests.post(discord_webhook_url, json=payload)
print(response.status_code)
print(response.text)
