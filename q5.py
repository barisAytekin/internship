import numpy as np
import pandas as pd
import statistics
df = pd.read_csv("./country_vaccination_stats.csv")
for i in range(df.shape[0]):
  if(np.isnan(df.iloc[i,2])):
    temp = df[df['country'] == df.iloc[i,0]]
    df.iloc[i,2] = temp['daily_vaccinations'].min()
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)
countries = {}
for i in range(df.shape[0]):
  if df.iloc[i, 0] not in countries.keys():
    countries[df.iloc[i, 0]] = [df.iloc[i, 2]]
  else:
    countries[df.iloc[i, 0]].append(df.iloc[i, 2])
for key in countries.keys():
  countries[key] = statistics.median(countries[key])
countries = sorted(countries.items(), key=lambda x: x[1], reverse = True)
for i in range(3):
  print(countries[i][0], "\n")