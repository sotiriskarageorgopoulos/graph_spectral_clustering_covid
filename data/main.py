import pandas as pd
# read csv to a dataframe
df = pd.read_csv('covid_19_test_cases.csv')
df_vac = pd.read_csv('eu_vaccinations.csv')
df_vac.rename(columns={'ReportingCountry': 'geoId'}, inplace=True)

# sum calculation  of cases and deaths for 2020 per country
df_2020 = df[df['year'] < 2021].groupby("geoId").agg(
    {'cases': sum, 'deaths': sum})

df_2020["IFR"] = df_2020["deaths"].div(df_2020["cases"].values)
df_2020.to_csv('covid_19(2020).csv')

# sum calculation  of cases and deaths for 2021-2022 per country
df_2021_2022 = df[df['year'] >= 2021].groupby("geoId").agg(
    {'cases': sum, 'deaths': sum})
df_2021_2022["IFR"] = df_2021_2022["deaths"].div(df_2021_2022["cases"].values)
df_vac_21_22 = df_vac[(df_vac['YearWeekISO'] >= '2021') & (df_vac["TargetGroup"] == "ALL")].groupby('geoId').agg({'FirstDose': sum, 'SecondDose': sum, 'DoseAdditional1': sum, 'DoseAdditional2': sum })

#dataframe with country codes
df2=df.groupby('geoId').agg('first').reset_index()
df3 = df2[['geoId']].copy()
df3.to_csv('eu_countries.csv')

covid_19_all = pd.merge(df_vac_21_22, df_2021_2022,
                  on='geoId',
                 how='inner')

covid_19_all.to_csv('covid_19(2021-2022).csv')