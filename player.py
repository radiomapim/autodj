import random

class AutoDJ:

    def __init__(self, playlist):

        self.playlist = playlist

    def proxima(self):

        return random.choice(self.playlist)
