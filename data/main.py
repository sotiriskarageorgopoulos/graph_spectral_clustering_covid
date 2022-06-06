import pandas as pd
# read csv to a dataframe
df = pd.read_csv('covid_19_test_cases.csv')

#dataframe with country codes
df2=df.groupby('geoId').agg('first').reset_index()
df3 = df2[['geoId']].copy()
df3.to_csv('eu_countries.csv')
# #dataframe for 2020(cases.deaths,countryterritoryCode)
df_20 = df[df['year'] < 2021].copy()
df20 = df_20[['cases', 'deaths', 'geoId']].copy()
df20.to_csv('covid_19(2020).csv')
# #dataframe for 2021-2022(cases.deaths,countryterritoryCode)
df_21_22 = df[df['year'] >= 2021].copy()
df21_22 = df_21_22[['cases', 'deaths', 'geoId']].copy()
df21_22.to_csv('covid_19(2021-2022).csv')