from pathlib import Path

def carregar_playlist(arquivo):

    musicas=[]

    with open(arquivo,"r",encoding="utf-8") as f:

        for linha in f:

            linha=linha.strip()

            if linha and not linha.startswith("#"):

                musicas.append(linha)

    return musicas
