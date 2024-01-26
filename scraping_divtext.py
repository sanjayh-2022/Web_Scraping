from bs4 import BeautifulSoup
import requests

class webscrape:
    def content(self, url):
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html5lib")
        for para in soup.find_all('div', class_="mw-content-ltr mw-parser-output"):
            print(para.text)

if __name__ == "__main__":
    web_obj = webscrape()
    web_obj.content("https://en.wikipedia.org/wiki/The_Avengers_(2012_film)")
