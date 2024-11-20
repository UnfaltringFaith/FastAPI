import pandas as pd
import numpy as np

anime = pd.read_csv("./anime.csv")
rating = pd.read_csv("./rating.csv")
#new = rating.merge(anime, left_on="anime_id", right_on="anime_id", suffixes=('_left', '_right'))

print(anime.groupby("episodes").count())