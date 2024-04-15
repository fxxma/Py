import pandas as pd

data = pd.read_csv("weather_data.csv")
hi = data.groupby(["day"])
print(hi)
