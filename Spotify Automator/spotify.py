import spotipy
import requests
from spotipy import client
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
track_uris=[]
result=sp.search(q=href,type="track",market="CA")
trackuri=(result['tracks']['items'][0]['uri'])
track_uris.append(trackuri)

my_play_list=sp_oth.user_playlist_create(user="pyytho",name="yooooo"
                                         ,public=False,description="this play list is made up of python script")

sp_oth.playlist_add_items(

)
# result=spotify.playlist_add_items(play_list_id=" ",items=" ",)
# sp.search(q=f"artist:{key} track:{value} year:{SONG_YEAR_YEAR}", type="track")
'http://spotifysentiment.com/callback'