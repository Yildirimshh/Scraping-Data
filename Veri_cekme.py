import requests
from bs4 import BeautifulSoup


url = requests.get("https://www.imdb.com/chart/top/")
if url.status_code == 200:
    print("You can extract data from the site.")
else:
    print("You can't extract data from the site.")

soup = BeautifulSoup(url.content,"html.parser")

no = 1
for i in soup.find("tbody",{"class":"lister-list"}).find_all("tr"):
    film_name = i.find("td",{"class":"titleColumn"}).a.text
    Year_take = i.find("span",{"class":"secoundaryInfo"}).text.strip("()")
    Rating_take = i.find("td",{"class":"imdbRating"}).strong.text
    print("..........film bilgisi.......")
    print(f"{say}:Film Name:{film_name}\nFilm Year:{Year_take}\nFilm Rating:{Rating_take}\n")
    no += 1