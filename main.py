
import requests
from bs4 import BeautifulSoup

answer_date = input("entre l'annee des sons que vous voulez sous format YY-MM-DDc: ")

##get data from Billboard site 

url = f"https://www.billboard.com/charts/hot-100/{answer_date}/#"

requet = requests.get(url)
website = requet.text

