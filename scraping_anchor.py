from bs4 import BeautifulSoup
import requests
class webscrape:
    def content(self,url):
      request=requests.get(url)
      soup=BeautifulSoup(request.content,"html5lib")
      for link in soup.find_all('a'):
        print(link.get("href"))
if __name__=="__main__":
  web_obj=webscrape()
  web_obj.content("https://en.wikipedia.org/wiki/The_Avengers_(2012_film)")