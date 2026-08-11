from playlist import carregar_playlist
from player import AutoDJ
from streamer import transmitir

playlist = carregar_playlist("playlists/segunda.m3u")

dj = AutoDJ(playlist)

while True:

    musica = dj.proxima()

    transmitir(musica)
