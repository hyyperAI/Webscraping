from bs4 import BeautifulSoup
import requests
website_data=requests.get('https://www.empireonline.com/movies/features/best-movies-2/')


soup=BeautifulSoup(website_data.text,'html.parser')

article=(soup.find_all(name="div" , class_="jsx-1456218620 article-content"))
for item in article:
    print(((item.find(name="div",class_="jsx-3523802742 listicle-item"))))
# main=soup.find_all(name="h3",class_='jsx-3523802742 block-item listicle-container ')
# print(main)
# article=main.find(name="article",class_="jsx-1456218620")
# second_div=article.find(name="div",class_="jsx-1456218620 article-content")
# main_div=second_div.find(name="div",class_="jsx-3523802742 block-item listicle-container")
# print(main_div.prettify())
# article_div=main_div.find_all(name="h3")
# print(article_div)


"""  H3 tag is dynamic means we is secured we cannot take control of it thrugh webscreaping  """