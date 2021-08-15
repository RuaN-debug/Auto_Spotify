# Auto Spotify

One day I was organizing some directories on my pc and I found the old songs I used to listen. I wanted to add those songs to a playlist on spotify, but there were like 300 songs, it would take ages to do it manually, so I decided to have python do it for me.

# How does it work?

It's quite simple: it saves the names of all the songs, without the extension, looks for their id's on spotify and adds the songs to the playlist you chose.

# How do I use it?

First of all, you need to have python installed in your pc, you can find the latest version here: https://www.python.org/downloads/

After that, you need to download this repository or clone it by using:
```sh
git clone git@github.com:RuaN-debug/Auto_Spotify.git
```
Now you need 3 things: the complete path of the directory with the songs in your pc, the id of the playlist you want to add the songs and a token to authorize that.
To get the playlist id you can go to spotify, copy the link of the playlist and the id will be the number after playlist/ and before the ?, like the example below:
```sh
https://open.spotify.com/playlist/0GfSUFhYrgdJfkIJO2kpbz?si=38b8654a512a4ddf
id = 0GfSUFhYrgdJfkIJO2kpbz
```
After getting the id you need the token to authorize python to do the work, you can get it by using the official api of spotify: https://developer.spotify.com/dashboard/login
Now, after logging in, you go to: https://developer.spotify.com/console/post-playlist-tracks/?playlist_id=0GfSUFhYrgdJfkIJO2kpbz&position=&uris= and paste the playlist id:

![image](https://user-images.githubusercontent.com/54671133/129482467-30623fc1-b56b-44dd-a9b2-9c0819e6c3de.png)

click on Get Token:

![image](https://user-images.githubusercontent.com/54671133/129482554-dd3d0f14-a300-44e6-8aae-60dc432035cd.png)

and mark the playlist-modify-public or playlist-modify-private, depending on the type of your playlist (public or private) and request the token.

![image](https://user-images.githubusercontent.com/54671133/129482596-f6a9e964-0c4a-43a2-9313-6842051bdc2a.png)

It will appear on the box to the left of the button. all you need to do is copy it.

Finally, you have everything you need, now in order to make it work you need to access the main.py file and paste the token and the path of the directory with the songs:

![image](https://user-images.githubusercontent.com/54671133/129482677-6811e723-3301-44ee-ac08-c387ee54dcd8.png)

then go to spotify_client and paste the id of your playlist:

![image](https://user-images.githubusercontent.com/54671133/129482705-fc5048d3-61dc-4a26-9f51-06320d796e48.png)

Now, all you have to do is to run the main.py file, you can do that with:
```sh
python main.py
```
Remember that the token is not permanent, you have to get another token every few minutes.
