from bs4 import BeautifulSoup
import requests

class webscrape:
    def content(self, url):
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html5lib")
        for para in soup.find_all('div', attrs={'class':"description"}):
             print(para.find('a')['title'], end='\n\n')

if __name__ == "__main__":
    web_obj = webscrape()
    web_obj.content("https://www.moneycontrol.com/news/")
