import os
from spotify_client import SpotifyClient, songs_not_found

token = 'Paste here your token with the rights to modify your playlist'
path_to_directory = r'Paste here the path to your directory with the songs'


def run():
    songs_aux = os.listdir(path_to_directory)
    songs = []
    for song in songs_aux:
        stripped = song.split('.', 1)[0]
        songs.append(stripped)

    spotify_client = SpotifyClient(token)

    for song in songs:
        song_ids = []
        spotify_song_id = spotify_client.search_song(song)
        if spotify_song_id:
            song_ids.append('spotify:track:' + spotify_song_id)
            added_song = spotify_client.add_song_to_spotify(song_ids)
            if added_song:
                print(f'{song} added successfully!')
    print(f'\nSongs that were not found:\n{songs_not_found}')


if __name__ == '__main__':
    run()
