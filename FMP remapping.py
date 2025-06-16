import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

load_dotenv()

df = pd.read_csv("./data/fmp remapping.csv")
df = df[df['FMPTicker'].notna()]

url = "https://financialmodelingprep.com/stable/search-symbol"
param = {
    "apikey": os.getenv("FMP_KEY"),
}

erroneous = set()
def get_data(row):
    tck = row['FMPTicker']

    params = param.copy()
    params['query'] = tck

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error: ", tck)
        erroneous.add(tck)
        return

    counter = 0
    for data_point in response.json():
        if data_point['symbol'] == tck:
            if counter:
                print("Multiple error: ", tck)
                erroneous.add(tck)
                return
            counter += 1

            row['FMP exchange'] = data_point['exchange']
            row['FMP name'] = data_point['name']

    if not counter:
        print(tck, "not found")
        erroneous.add(tck)
        print(json.dumps(response.json(), indent=4))
        return

    return row


# df = df.truncate(before=2917, after=2917)

print(df)


with ThreadPoolExecutor(max_workers=50) as executor:
    status = list( executor.map(get_data, (row for _, row in df.iterrows())) )

df2 = pd.DataFrame(status)
df2.to_csv("./data/fmp remapping extracted.csv", index=False)

pd.set_option('display.width', None)
print(type(status[0]), status)
print("status: \n", pd.DataFrame(status))
print("Errors: ", erroneous)

