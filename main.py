import requests
import hashlib
import os

url = "https://httpbin.org/uuid"  # Ensure you're testing with this URL
hash_file = "previous_hash.txt"

discord_webhook_url = "https://discord.com/api/webhooks/1291521698587218051/D6Ty9uc_fY3NZKvsB_bQqepF3SWpc_TTh5KkR1wobGkW-Dfe8WJbrfQ4sRRzouddchoh"  # Update to use env variable or set directly

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def get_hash(content):
    content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
    print(f"Current Hash: {content_hash}")  # Log current hash
    return content_hash

def check_for_changes():
    content = fetch_website_content(url)
    print(content)  # Log fetched content
    if content is None:
        return
    
    current_hash = get_hash(content)

    if os.path.exists(hash_file):
        with open(hash_file, 'r') as file:
            previous_hash = file.read().strip()
            print(f"Previous Hash: {previous_hash}")  # Log previous hash

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
