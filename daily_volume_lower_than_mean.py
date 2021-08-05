import pandas as pd

df = pd.read_csv('./AAPL.csv')

mean_daily_volume = df["Volume"].mean()
print("The arithmetic mean of the daily volume in this dataset is " + str(round(mean_daily_volume, 1)))
print("The number of days where the daily volume is below the arithmetic mean is " + str(df[df["Volume"] < mean_daily_volume].shape[0]))
