import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Apple.csv",low_memory=False)
df.set_index("Date",inplace=True)

prices = df['Close'].to_numpy()
dates = df.index.to_numpy()

import gc
from pathlib import Path

def make_dataset(dates,prices,window_size=20,path="Dataset"):

  path = Path(path)
  path.mkdir(exist_ok=True)

  up_dir = path / 'up'
  up_dir.mkdir(exist_ok=True)

  down_dir = path / 'down'
  down_dir.mkdir(exist_ok=True)



  dates = dates
  prices = prices

  for i in range(len(dates)-window_size):
    dates_range = dates[i:i+window_size]
    prices_range = prices[i:i+window_size]
    next_price = prices[i+window_size]
    figure = plt.figure(figsize=(16,13),facecolor="black")
    ax = plt.axes()
    ax.set_facecolor("black")
    plt.plot(dates_range,prices_range,color="white")

    if prices_range[-1] > next_price:
      figure.savefig(str(path)+"/down/"+str(i)+".jpg")
    else:
      figure.savefig(str(path)+"/up/"+str(i)+".jpg")

    plt.close()
    gc.collect()

    print(str(i) + " was done")


make_dataset(dates[4500:5200],prices[4500:5200],path="Valid")
make_dataset(dates[5200:],prices[5200:],path="Test")