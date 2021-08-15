import requests
import json

songs_not_found = []
playlist_id = 'Paste here your playlist id'


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def search_song(self, track):
        url = f"https://api.spotify.com/v1/search?q={track}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response.raise_for_status()
        response_json = response.json()

        results = response_json['tracks']['items']
        if results:
            return results[0]['id']
        else:
            print(f'{track} was not found!')
            songs_not_found.append(track)
            return None

    def add_song_to_spotify(self, song_ids):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        request_body = json.dumps({"uris": song_ids})

        response = requests.post(
            url,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        return response.ok
