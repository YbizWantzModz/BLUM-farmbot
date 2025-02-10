import requests
import time

CLOUD_ACCOUNTS_URL = "https://example.com/blum_accounts.json"  # Замените на реальный URL

def get_accounts():
    try:
        print("[INFO] Fetching accounts from the cloud...")
        response = requests.get(CLOUD_ACCOUNTS_URL)
        if response.status_code == 200:
            accounts = response.json().get("accounts", [])
            print(f"[INFO] Loaded {len(accounts)} accounts.")
            return accounts
        else:
            print(f"[ERROR] Failed to load accounts. HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"[ERROR] Could not retrieve accounts: {e}")
        return []

if __name__ == "__main__":
    print("Testing cloud connection...")
    time.sleep(2)
    get_accounts()
