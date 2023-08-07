import bs4
import requests
import spotipy

    # REQUEST MODULE

date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
website=requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = bs4.BeautifulSoup(website.text, "html.parser")

all_list = (soup.find_all(name="ul",
                          class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"))

all_names = [(((item.find(name="h3", id="title-of-a-story")).text).strip()) for item in all_list]
print(all_names)

#  setting up SPOTIFY SYSTEMS

my_id="53ccc935341c40da9d4b29e2cb680d84"
my_secret="4614d1a02ec64d5c9bdd9ab911b01b81"
redirect="https://open.spotify.com/artist/4yvcSjfu4PC0CYQyLy4wSq"
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'
query=f"artist:'Glass Animals' track: 'Heat Waves' "
href=f"https://api.spotify.com/v1/search?query={query} type: track"
"&include_external=audio&market=US&locale=en-US%2Cen%3Bq%3D0.9&offset=1&limit=1"


sp_oth=spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=my_id
                                                         ,client_secret=my_secret
                                                         ,redirect_uri=" http://localhost:3000/callback/ "
                                                         ,show_dialog=True,cahe_path="token.txt"))

sp=spotipy.Spotify(client_credentials_manager=spotipy.SpotifyClientCredentials(client_id=my_id,
                                        client_secret=my_secret))

spotify_id = sp.current_user()["id"]

track_uris=[]
for item in all_names:
    result=sp.search(q=f"track:{item}",type="track",market="CA")
    trackuri=(result['tracks']['items'][0]['uri'])
    track_uris.append(trackuri)

# create a private playlist base on the date the user inputted

playlist = sp.user_playlist_create(
    user=spotify_id,
    name=f"{date} Billboard 100",
    public=False,
)

# Add track uris to the newly created playlist
sp_oth.playlist_add_items(
    user=spotify_id,
    playlist_id=playlist['id'],
    tracks=track_uris,
)