import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import uuid



date_field = "Date"
price_field = "Price"
print("Loading data..")

df = pd.read_csv("BNB_USD Binance Historical Data.csv",low_memory=False)
df.set_index(date_field,inplace=True)

print("data fully loaded")
prices = df[price_field].to_numpy()
dates = df.index.to_numpy()

import gc
from pathlib import Path

def make_dataset(dates,prices,window_size=50,path="Dataset"):

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
    # ax.set_facecolor("black")
    ax.fill_between(dates_range,prices_range,color="orange")
    plt.plot(dates_range,prices_range,color="red")
    plt.scatter(dates_range,prices_range,color="blue")


    if prices_range[-1] > next_price:
      figure.savefig(str(path)+"/down/"+str(uuid.uuid4())+".jpg")
    else:
      figure.savefig(str(path)+"/up/"+str(uuid.uuid4())+".jpg")

    # plt.show()
    plt.close()
    gc.collect()

    print(str(i) + " was done")



make_dataset(dates,prices,path="TrainDatasetV4")
# make_dataset(dates[700:900],prices[700:900],path="ValidV4")
# make_dataset(dates[900:1100],prices[900:1100],path="TestV4")

# make_dataset(dates[:3500],prices[:3500],path="TrainDataset")
# make_dataset(dates[3500:4000],prices[3500:4000],path="Valid")
# make_dataset(dates[4000:-1],prices[4000:-1],path="Test")
