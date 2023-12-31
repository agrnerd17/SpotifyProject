#authorization code flow:
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#func to retrieve token:
def get_token():
    author_str = client_id + ":" + client_secret
    author_bytes = author_str.encode("utf-8")
    author_base64 = str(base64.b64encode(author_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + author_base64,
        "Content-Type": "application/x-www-form-urlencoded"

    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data) #body of request
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

#gets authorization header, returns token
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

#implements spotify's api and searches for artist name
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1" #can do more than one: i.e., artist_name, song etc

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artists with this name exists...")
        return None
    return json_result[0]

def get_songs_by_artists(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result



token = get_token()
result = search_for_artist(token, "Doja Cat") #returns doja cat's top 10 tracks
artist_id = result["id"]
songs = get_songs_by_artists(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}") #formats the top 10 songs by number and song title
