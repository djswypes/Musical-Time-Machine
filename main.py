from musicsearch import MusicSearch
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

musicSearch = MusicSearch()
all_songs = musicSearch.get_songs()
date = musicSearch.date

scope = "playlist-read-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()['id']
year = date.split('-')[0]
song_uris = []
for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

create_playlist = sp.user_playlist_create(user=user_id, name=date + 'Billboard 100', public=False)
playlist_id = create_playlist['id']
sp.playlist_add_items(playlist_id, song_uris, position=None)

