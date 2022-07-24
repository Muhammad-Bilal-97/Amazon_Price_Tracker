import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B06XQBNFT7/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

header = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en-GB;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(name="span", class_ = "a-price-whole").getText()
price_without_currency = price.split("$")[0]
price_as_float = float(price_without_currency)
print(price_as_float)


title = soup.find(id="productTitle").getText().strip()
print(title)


BUY_PRICE = 40
YOUREMAIL = "bilalroze94@gmail.com"

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(smtp.gmail.com, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUREMAIL, password="BIaq#123a")
        connection.sendmail(
            from_addr=YOUREMAIL,
            to_addrs=YOUREMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )






