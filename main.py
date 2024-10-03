import requests

discord_webhook_url = "https://discord.com/api/webhooks/1287762242300809277/oo7Lw_5xgLnX4nBMWHIQCql3xL_9JoMIpe7YKzX7NLl0Y_WQOXu51czoA9S37C1mxxjz"

payload = {
    "content": "NIHAOOOOOOOOOOOOOOOOOOOOOO",
    "username": "Test Bot"
}

response = requests.post(discord_webhook_url, json=payload)
print(response.status_code)
print(response.text)
