from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.example.com")

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "example-table"})

rows = table.find_all("tr")
data = []
for row in rows:
    cols = row.find_all("td")
    cols = [col.text for col in cols]
    data.append(cols)

import pandas as pd
df = pd.DataFrame(data, columns=["Column 1", "Column 2", "Column 3"])
