from bs4 import BeautifulSoup
import requests


class MusicSearch:
    def __init__(self):
        self.date = None
        self.songs = None

    def get_songs(self):
        self.date = input('What year you would like to travel to in YYY-MM-DD format: ')
        URL = f'https://www.billboard.com/charts/hot-100/{self.date}'
        response = requests.get(URL)
        response.raise_for_status()
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        self.songs = [a.getText().strip() for a in soup.select("li #title-of-a-story")]
        return self.songs
