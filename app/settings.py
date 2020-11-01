#  Client Keys
SPOTIPY_CLIENT_ID = "fe0d68927c804ef7a0d0cc3fa17ce096"
SPOTIPY_CLIENT_SECRET = "941c645d1a0745e69cdd4fef29611f9b"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
SPOTIPY_REDIRECT_URI = 'http://localhost:8888'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

PORT = 8000
STATE = ""
SHOW_DIALOG_bool = False
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": SPOTIPY_REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": SPOTIPY_CLIENT_ID
}
