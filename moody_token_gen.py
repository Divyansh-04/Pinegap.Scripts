import requests
import os
from dotenv import load_dotenv, set_key

load_dotenv()

url = "https://token.hub.moodysanalytics.com/prod/auth/token"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
    "Authorization": os.getenv("M_TOKEN_GENERATOR"),
    "Content-Type": "application/json",
    "Origin": "https://docs.moodysanalytics.com",
    "Referer": "https://docs.moodysanalytics.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15",
    "Cookie": "__cf_bm=ndiL4J1mVx7fe.sj8KG3chZjbAyuVaa62DF01RBTG4Q-1747833427-1.0.1.1-oU8zms8YkPLQtfnHOGoaO.WTBuDCNtl4hXUHGzIbYdtvekUHr9yya8XTioLPmaFobYQjX8AAHzgHSuY.PGVwsfm6lqzeaQ5Ch6Lx0UNXUJo"
}

r = requests.post(url, headers=headers)
print(r.status_code)
print(r.json()["access_token"])

set_key(".env", "M_TOKEN", r.json()["access_token"])
