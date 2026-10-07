import requests
import time
import os

# GitHub Secrets se tokens uthata hai
TOKEN = os.getenv("TOKEN")
AR_TOKEN = os.getenv("AR_TOKEN")

# API URL
url = "https://ok888.win/WinGo/WinGo_30S/GetHistoryIssuePage.json"

# Cache se bachne ke liye dynamic timestamp
params = {"ts": int(time.time() * 1000)}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Authorization": f"Bearer {TOKEN}",
    "ar-token": AR_TOKEN,
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://ok888.win/WinGo/WinGo_30S"
}

# API call
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print("✅ Data mil gaya!")
    print(response.json())
else:
    print(f"❌ Error aaya. Status Code: {response.status_code}")
    print(response.text)
