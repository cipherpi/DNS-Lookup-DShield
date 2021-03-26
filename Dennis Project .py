import requests
import json
import pandas as pd
domain = input ("Insert your URL: " )
url = f"https://isc.sans.edu/api/dnslookup/{domain}?json"
print(f"url: {url}")
response = requests.get(url)
df = pd.read_json(response.text)
print(df)
