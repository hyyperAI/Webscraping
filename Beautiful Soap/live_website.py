from bs4 import BeautifulSoup
import requests

y_combinator = requests.get("https://news.ycombinator.com/")
yc_web_page = (y_combinator.text)

soup = BeautifulSoup(yc_web_page, 'html.parser')

a_tag = (soup.find(name='span', class_="titleline"))

article_tag = a_tag.getText()[0:a_tag.getText().index('(')]
article_link = a_tag.a.get('href')
article_upvote = soup.find(name="span", class_="score")


all_tag=soup.find_all(name='span',class_='titleline')
articles_tag=[articles.getText()[0:a_tag.getText().index('(')] for articles in all_tag]
articles_link=[articles.a.get('href')  for articles in all_tag]

all_scores=[int(score.getText().split(" ")[0])  for score in soup.find_all(name='span',class_='score') ]
largest_index=(all_scores.index(max(all_scores)))

print(articles_tag[largest_index])
print(articles_link[largest_index])

print(all_scores[largest_index])

