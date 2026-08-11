import subprocess
from config import *

def transmitir(musica):

    comando=[

        "ffmpeg",

        "-re",

        "-i",musica,

        "-vn",

        "-codec:a","libmp3lame",

        "-b:a",BITRATE,

        "-ar",SAMPLERATE,

        "-content_type","audio/mpeg",

        f"icecast://source:{PASSWORD}@{HOST}:{PORT}/stream"

    ]

    subprocess.run(comando)
