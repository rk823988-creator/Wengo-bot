import requests
import time
import os
from supabase import create_client, Client

# GitHub Secrets se tokens uthata hai
TOKEN = os.getenv("TOKEN")
AR_TOKEN = os.getenv("AR_TOKEN")

# Supabase Secrets
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Supabase client banao
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# API URL
url = "https://ok888.win/WinGo/WinGo_30S/GetHistoryIssuePage.json"

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
    data = response.json()
    if 'data' in data and 'list' in data['data']:
        results = data['data']['list']
        print(f"Total {len(results)} records mile. Supabase me save kar rahe hain...")
        
        saved_count = 0
        for item in results:
            period = int(item['issueNumber'])
            number = int(item['number'])
            color = item['color']
            
            try:
                # Data ko Supabase me save karo (Duplicate check ke saath)
                supabase.table('results').upsert(
                    {"period": period, "number": number, "color": color},
                    on_conflict="period"
                ).execute()
                saved_count += 1
            except Exception as e:
                print(f"❌ Error {period}: {e}")
                
        print(f"✅ {saved_count} records successfully save ho gaye!")
    else:
        print("❌ Data format galat hai.")
else:
    print(f"❌ API Error. Status Code: {response.status_code}")
