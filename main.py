from bs4 import BeautifulSoup
import requests
from  spotipy.oauth2 import SpotifyOAuth
import spotipy
date=input("which year do you want to travel to? Type the data in this format YYYY-MM-DD:")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
data=requests.get(url="https://www.billboard.com/charts/hot-100/" + date,headers=header)
print(data.raise_for_status)
contents=data.text
soup=BeautifulSoup(contents,"html.parser")
song_names_spans=soup.select("li ul li h3")
# print(song_names_spans)
song_names=[ song.getText().strip() for song in song_names_spans]
print(song_names)
Client_id="YOUR SPOTIFY CLIENT ID"
Client_secret="YOUR SPOTIFY CLIENT SECRET"
sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_id,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR SPOTIFY ACCOUNT USERNAME"

    )

)
user_id=sp.current_user()['id']
print(user_id)
song_uris=[]
year=date.split("-")[0]
for song in song_names:
    result=sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped.")

playlist=sp.user_playlist_create(user='SPOTIFY ACCOUNT USERNAME',name=f"{date} Billboard 100",public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)
