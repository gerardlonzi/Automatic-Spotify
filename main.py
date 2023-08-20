
import requests
from bs4 import BeautifulSoup

answer_date = input("entre l'annee des sons que vous voulez sous format YY-MM-DD: ")

##get data from Billboard site 

url = f"https://www.billboard.com/charts/hot-100/{answer_date}/#"

requet = requests.get(url)
website = requet.text

soup = BeautifulSoup(website,'html.parser')

##parsing data 
song_name = []
All_song = soup.find_all(name='span',class_ ='a-truncate-ellipsis-2line')

for song in All_song:
    print(song.getText())
    song_name.append(song.getText())
    


