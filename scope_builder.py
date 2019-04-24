class ScopeBuilder:

    def __init__(self):
        self.scopes = []

    def listening_history(self):
        self.scopes.append('user-read-recently-played')
        self.scopes.append('user-top-read')

        return self

    def library(self):
        self.scopes.append('user-library-modify')
        self.scopes.append('user-library-read')

        return self

    def playlists(self):
        self.scopes.append('playlist-read-private')
        self.scopes.append('playlist-modify-public')
        self.scopes.append('playlist-modify-private')
        self.scopes.append('playlist-read-collaborative')

        return self

    def users(self):
        self.scopes.append('user-read-email')
        self.scopes.append('user-read-birthdate')
        self.scopes.append('user-read-private')

        return self

    def spotify_connect(self):
        self.scopes.append('user-read-playback-state')
        self.scopes.append('user-modify-playback-state')
        self.scopes.append('user-read-currently-playing')

        return self

    def playback(self):
        self.scopes.append('app-remote-control')
        self.scopes.append('streaming')

        return self

    def follow(self):
        self.scopes.append('user-follow-read')
        self.scopes.append('user-follow-modify')

        return self

    def get_scopes(self):
        ret = ""
        for scope in self.scopes:
            ret += "%s " % scope
        return ret
