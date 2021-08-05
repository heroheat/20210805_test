import pandas as pd

df = pd.read_csv('./AAPL.csv')

median_daily_volume = df["Volume"].median()
print("The arithmetic mean of the daily volume in this dataset is " + str(median_daily_volume))
print("The number of days where the daily volume is below the arithmetic mean is " + str(df[df["Volume"] < median_daily_volume].shape[0]))
