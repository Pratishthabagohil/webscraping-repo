import pandas as pd
import requests
from bs4 import BeautifulSoup

product = []
prices = []
description = []
reviews = []

for i in range(1, 12): 
    url = f"https://www.flipkart.com/search?q=mobile+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    containers = soup.find_all("div", class_="_1AtVbE")
    
    if not containers:
        print("No product containers found on page", i)
        continue
    
    for container in containers:
        name_tag = container.find("div", class_="_4rR01T")
        price_tag = container.find("div", class_="_30jeq3")
        desc_tag = container.find("ul", class_="_1xgFaf")
        review_tag = container.find("div", class_="_3LWZlK")

        if name_tag:
            product.append(name_tag.strip())
        else:
            product.text.append(None)

        if price_tag:
            prices.append(price_tag.text.strip())
        else:
            prices.append(None)

        if desc_tag:
            description.append(desc_tag.text.strip())
        else:
            description.append(None)

        if review_tag:
            reviews.append(review_tag.text.strip())
        else:
            reviews.append(None)

df = pd.DataFrame({"Product Name": product, "Prices": prices, "Description": description, "Reviews": reviews})
print(df)
df.to_csv("fl.csv", index=False)
