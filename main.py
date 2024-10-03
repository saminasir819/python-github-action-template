import requests
import hashlib
import os

url = "https://httpbin.org/uuid"
discord_webhook_url = "https://discord.com/api/webhooks/1287762242300809277/oo7Lw_5xgLnX4nBMWHIQCql3xL_9JoMIpe7YKzX7NLl0Y_WQOXu51czoA9S37C1mxxjz"
hash_file = "previous_hash.txt"

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def get_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def check_for_changes():
    content = fetch_website_content(url)
    if content is None:
        return

    current_hash = get_hash(content)

    if os.path.exists(hash_file):
        with open(hash_file, 'r') as file:
            previous_hash = file.read()

        if previous_hash == current_hash:
            print("No changes detected.")
        else:
            print("Website has changed!")
            trigger_alert()

    with open(hash_file, 'w') as file:
        file.write(current_hash)

def trigger_alert():
    message = {
        "content": f"ALERT! The content of {url} has changed.",
        "username": "Website Monitor"
    }
    try:
        response = requests.post(discord_webhook_url, json=message)
        response.raise_for_status()
        print("Alert sent to Discord!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending alert to Discord: {e}")

if __name__ == "__main__":
    check_for_changes()
