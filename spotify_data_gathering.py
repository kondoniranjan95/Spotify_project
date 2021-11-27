import config
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
from time import sleep
from random import randint


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.client_id,
                                                           client_secret=config.client_secret))

playlist = sp.user_playlist_tracks("spotify", "2LOxEzC4KmoWJ9NhW0kz5M",market="GB")