import requests
import re

url = "https://www.bbc.com/news"

try:
    response = requests.get(url)
    response.raise_for_status()
    html = response.text

    headlines = re.findall(r'<h3.*?>(.*?)</h3>', html, re.DOTALL)
    count = 0
    print("Top news headlines:\n")
    for h in headlines:
        text = re.sub('<.*?>', '', h).strip()
        if text:
            count += 1
            print(f"{count}. {text}")
        if count == 10:
            break

except Exception as e:
    print("Error:", e)

