import bs4
import requests
website_url="https://www.amazon.com/Alpina-Alpiner-Swiss-Quartz-Watch/dp/B0BN2C35PX?ref_=ast_sto_dp&th=1&psc=1"


website=requests.get(url=website_url)
print(website.text)
# soup=bs4.BeautifulSoup(website.text,"html.parser")
# print(soup)
# print(soup.find_all(name="div",id="apex-desktop"))