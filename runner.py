import sys
from client import Spotify
import util as util
from auth_values import AuthValues
from scope_builder import ScopeBuilder
import pickle

store = {}
try:
    with open('store.pkl', 'rb') as f:
        store = pickle.load(f)
except FileNotFoundError:
    print("No existing store")

store['test_id'] = "spotify:user:andrew_walker2:playlist:6VXKlqxCX4ItIHWgFT9I6c"

scope = ScopeBuilder().library().spotify_connect().get_scopes()

auth = AuthValues()

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id=auth.CLIENT_ID, client_secret=auth.CLIENT_SECRET,
                                   redirect_uri=auth.REDIRECT_URL)

device = None

if token:
    sp = Spotify(auth=token)
    devices = sp.devices()
    devices = devices['devices'][0]['id']
else:
    print("Can't get token for", username)

with open('store.pkl', 'wb') as f:
    pickle.dump(store, f, pickle.HIGHEST_PROTOCOL)
