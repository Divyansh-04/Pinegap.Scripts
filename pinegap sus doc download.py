import os
import requests
import pandas as pd


def download(url, path):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
        return "downloaded"
    except Exception as e:
        print(e, url)
        return f"failed {e}"


df = pd.read_csv(r"data\sus press 2.csv")
print(len(df))



# with ThreadPoolExecutor(max_workers=100) as executor:
#     status = list(executor.map(download, df["url"].tolist(), df["path"].tolist())
