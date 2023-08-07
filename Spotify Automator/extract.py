import bs4
import requests

class Scrapper(bs4):

    def __int__(self,url):
        super().__init__()
        self.url=url
        self.songs=[]
        self.artist=[]
        self.text = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.text.txt, "parser.html")

    def songs(self):
        all_list = (self.soup.find_all(name="ul",
        class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"))
        [self.songs.append(((item.find(name="h3", id="title-of-a-story")).text).strip()) for item in all_list]
        return self.songs
    def artists(self):
        all_artist=self.soup.find_all(name="h3")


website = requests.get(url="https://www.billboard.com/charts/hot-100/")

# soup = BeautifulSoup(website.text, "html.parser")
#
# all_list = (soup.find_all(name="ul",
#                           class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"))
# # all_list=(soup.find_all(name="li",class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex
# # lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max
# # lrv-u-border-color-grey-light  lrv-u-padding-l-1@mobile-max"))
# names = [(((item.find(name="h3", id="title-of-a-story")).text).strip()) for item in all_list]
# print(names[0])
