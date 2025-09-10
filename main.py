from bs4 import BeautifulSoup
import requests
import smtplib
import lxml

email = "redbullwithfanta@gmail.com"
password = "pxep shbv kyys ullh"
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}
response = requests.get(url, headers=header).text
soup = BeautifulSoup(response,"lxml")
# print(soup)
whole = soup.select(".a-price-whole")[0].getText()
point = soup.select(".a-price-fraction")[0].getText()
price = whole + point
# print(price)


connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=email, password=password)

if float(price) < 100:
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg=f"Subject:Big Ass Discount!\n\nThe current price of the product is {price}"
    )