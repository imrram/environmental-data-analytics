import requests
import pandas as pd

# Example: Get PM2.5 data for Delhi
url = "https://api.openaq.org/v2/measurements?city=Delhi&parameter=pm25&limit=1000"
res = requests.get(url)
data = res.json()['results']
df = pd.DataFrame(data)
df.to_csv("delhi_pm25.csv", index=False)
