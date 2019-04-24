import sys
from client import Spotify
import spotipy.util as util
from auth_values import AuthValues
from scope_builder import ScopeBuilder

scope = ScopeBuilder().library().spotify_connect().get_scopes()

auth = AuthValues()

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id=auth.CLIENT_ID, client_secret=auth.CLIENT_SECRET,
                                   redirect_uri=auth.REDIRECT_URL)

if token:
    sp = Spotify(auth=token)

    print(sp.current_user())
    print(sp.devices())
    devices = sp.devices()
    sp.play_track("spotify:user:andrew_walker2:playlist:6VXKlqxCX4ItIHWgFT9I6c", devices['devices'][0]['id'])

else:
    print("Can't get token for", username)
