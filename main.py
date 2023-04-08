import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import uuid


print("Loading data..")

df = pd.read_csv("BTC.csv",low_memory=False)
df.set_index("Date",inplace=True)

print("data fully loaded")
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
      figure.savefig(str(path)+"/down/"+str(uuid.uuid4())+".jpg")
    else:
      figure.savefig(str(path)+"/up/"+str(uuid.uuid4())+".jpg")


    plt.close()
    gc.collect()

    print(str(i) + " was done")



make_dataset(dates[:2000],prices[:2000],path="TrainDataset")
make_dataset(dates[2000:2500],prices[2000:2500],path="Valid")
make_dataset(dates[2500:3000],prices[2500:3000],path="Test")

# make_dataset(dates[:3500],prices[:3500],path="TrainDataset")
# make_dataset(dates[3500:4000],prices[3500:4000],path="Valid")
# make_dataset(dates[4000:-1],prices[4000:-1],path="Test")
