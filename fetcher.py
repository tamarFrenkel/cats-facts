import requests
import pandas as pd

def fetch_api_data(url, n=10):

    records = []

    for i in range(n):
        print(f"Fetching fact {i+1}/{n}...")
        resp = requests.get(url, timeout=10, verify=False)
        resp.raise_for_status()
        data = resp.json()
    
        records.append({
            "fact": data.get("fact", ""),
            "length": data.get("length", 0)
        })
    
    df = pd.DataFrame(records)
    return df
