from bs4 import BeautifulSoup
import requests


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

responce = requests.get(URL)
soup = BeautifulSoup(responce.content, 'lxml')
#print(soup.prettify())
hi = soup.find_all(name= "h3", class_="title")
hi_title = [movie.getText() for movie in hi]
for n in range(len(hi_title)-1,0,-1):
    print(hi_title[n])
    with open('hi_title.txt','w') as file:
        file.write(hi_title[n])