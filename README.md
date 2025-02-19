I recently completed where I combined multiple Python libraries and APIs to automate the creation of a Billboard Hot 100 Playlist in a Spotify account!
This project gave me hands-on experience with web scraping, API authentication, and automation.

let see implementation part step by step..

Step 1 - Scraping the Billboard Hot 100

1. Create a new project in PyCharm and create the main.py file.

2. Create an input() prompt that asks what year you would like to travel to in YYY-MM-DD format. e.g.

3. Include a header when you make your request to billboard.com.

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


4. Using  BeautifulSoup, scrape the top 100 song titles on that date into a Python List.

Hint: Take a look at the URL of the chart on a historical date: https://www.billboard.com/charts/hot-100/2000-08-12


Step 2 - Authentication with Spotify



1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:

https://developer.spotify.com/dashboard/

3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.

Spotify uses OAuth to allow third-party applications (e.g. our Python code) to access a Spotify user's account without giving them the username or password. We'll explore OAuth more in later modules on web development, but if you want you can read more about it here: https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth

Authenticating with Spotify is quite complicated, especially when you want to access a user's account. So instead, we're going to use one of the most popular Python Spotify modules - Spotipy to make things easier.


4. Using the Spotipy documentation,  authenticate your Python project with Spotify using your unique Client ID/ Client Secret.


5. Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.

HINT 1: You need your own Spotify app Client ID and Secret, the ones in the image above won't work.

HINT 2: This is the method you'll need: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth

HINT 3: Try passing the Client ID and Secret directly into the SpotifyOAuth() constructor instead of using export or set.

HINT 4: You need the "playlist-modify-private" scope in order to create a private playlist on Spotify.

HINT 5:  If successful, you should see the page show up automatically (be sure to click Agree):

Then it will take you to the page , example.com and you need to copy the entire URL in the address bar:

Finally, you need to paste the URL into the prompt in PyCharm:

Now if you close PyCharm and restart, you should see a new file in this project called token.txt

5. Get the user id of the authenticated user (your Spotify username).

HINT 1: You'll need this method: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user

HINT 2: The output of the above method is a dictionary, look for the value of the "id" key.

HINT 3: If you see the error "HTTP Error for GET to https://api.spotify.com/v1/me/ with Params: {} returned 403 due to User not registered in the Developer Dashboard" double check you are passing a username during the authorisation flow. 


Step 3 - Search Spotify for the Songs from Step 1


1. Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).

HINT 1: You can use the query format "track: {name} year: {YYYY}" to narrow down on a track name from a particular year.

HINT 2: Sometimes a song is not available in Spotify, you'll want to use exception handling to skip over those songs.

HINT 3: pprint() might help you visualise the result better. https://docs.python.org/3/library/pprint.html


Step 4 - Creating and Adding to Spotify Playlist


1. Using the Spotipy documentation, create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date you inputted in step 1.

HINT: You'll need the user id you got from Step 2.

2. Add each of the songs found in Step 3 to the new playlist.

HINT: You'll need the playlist id which is returned as an output once you've successfully created a new playlist.
