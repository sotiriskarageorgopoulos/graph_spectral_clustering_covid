import pandas as pd
import warnings
warnings.filterwarnings("ignore")
# read csv to a dataframe
df = pd.read_csv('covid_19_test_cases.csv')
df_vac = pd.read_csv('eu_vaccinations.csv')
df_vac.rename(columns={'ReportingCountry': 'geoId'}, inplace=True)

# sum calculation of cases and deaths for 2020 per eu country
df_2020 = df[df['year'] < 2021].groupby("geoId").agg(
    {'cases': sum, 'deaths': sum})

df_2020["IFR"] = df_2020["deaths"].div(df_2020["cases"].values)
df_2020.to_csv('eu_covid_19(2020).csv')

# sum calculation of cases and deaths for 2021-2022 per eu country
df_2021_2022 = df[df['year'] >= 2021].groupby("geoId").agg(
    {'cases': sum, 'deaths': sum})
df_2021_2022["IFR"] = df_2021_2022["deaths"].div(df_2021_2022["cases"].values)
df_vac_21_22 = df_vac[(df_vac['YearWeekISO'] >= '2021') & (df_vac["TargetGroup"] == "ALL")].groupby('geoId').agg({'FirstDose': sum, 'SecondDose': sum, 'DoseAdditional1': sum, 'DoseAdditional2': sum })

covid_19_all = pd.merge(df_vac_21_22, df_2021_2022,
                  on='geoId',
                 how='inner')

covid_19_all.to_csv('eu_covid_19(2021-2022).csv')

def create_csv_by_continent(world_data:pd.DataFrame,continent:str,period:str):
    cond_cases_vacc = ""
    cond_deaths_vacc = ""
    if period == "after":
        cond_cases_vacc = (~world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'cases') & (world_data["year_week"].str.contains("2021") | world_data["year_week"].str.contains("2022")) & (world_data["continent"] == continent)
        cond_deaths_vacc  = (~world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'deaths') & (world_data["year_week"].str.contains("2021") | world_data["year_week"].str.contains("2022")) & (world_data["continent"] == continent)
    elif period == "before":
        cond_cases_vacc = (~world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'cases') & (world_data["year_week"].str.contains("2020")) & (world_data["continent"] == continent)
        cond_deaths_vacc = (~world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'deaths') & (world_data["year_week"].str.contains("2020")) & (world_data["continent"] == continent)
    else:
        print("Wrong period...")
   
    cases_vacc = world_data[cond_cases_vacc].groupby('country_code')["weekly_count"].sum()
    deaths_vacc = world_data[cond_deaths_vacc].groupby('country_code')["weekly_count"].sum()
    new_df = pd.merge(cases_vacc,deaths_vacc,on="country_code",how="inner")
    new_df.rename(columns={'weekly_count_x': 'cases'}, inplace=True)
    new_df.rename(columns={'weekly_count_y': 'deaths'}, inplace=True)
    new_df["IFR"] = new_df["deaths"].div(new_df["cases"].values)
    
    if period == "before":
        new_df.to_csv(f"{continent.lower()}_continent_covid(2020).csv")
    elif period == "after":
        new_df.to_csv(f"{continent.lower()}_continent_covid(2021-2022).csv")

world_data = pd.read_csv("../data/worldwide_data.csv")

#Europe continent stats before vaccinations
create_csv_by_continent(world_data,"Europe","before")
#Europe continent stats after vaccinations
create_csv_by_continent(world_data,"Europe","after")

#Asia continent stats before vaccinations
create_csv_by_continent(world_data,"Asia","before")
#Asia continent stats after vaccinations
create_csv_by_continent(world_data,"Asia","after")

#Oceania continent stats before vaccinations
create_csv_by_continent(world_data,"Oceania","before")
#Oceania continent stats after vaccinations
create_csv_by_continent(world_data,"Oceania","after")

#America continent stats before vaccinations
create_csv_by_continent(world_data,"America","before")
#America continent stats after vaccinations
create_csv_by_continent(world_data,"America","after")

def create_continents_csv(world_data,period):
    cond_cases_continents = ""
    cond_deaths_continents = ""
    if period == 'before':
        cond_cases_continents = (world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'cases') & (~world_data["country"].str.contains("EU/EEA")) & (world_data["year_week"].str.contains("2020"))
        cond_deaths_continents = (world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'deaths') & (~world_data["country"].str.contains("EU/EEA")) & (world_data["year_week"].str.contains("2020"))
    elif period == 'after':
        cond_cases_continents = (world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'cases') & (~world_data["country"].str.contains("EU/EEA")) & (world_data["year_week"].str.contains("2021") | world_data["year_week"].str.contains("2022"))
        cond_deaths_continents = (world_data["country"].str.contains("(total)")) & (world_data["indicator"] == 'deaths') & (~world_data["country"].str.contains("EU/EEA")) & (world_data["year_week"].str.contains("2021") | world_data["year_week"].str.contains("2022"))
    
    continents_cases = world_data[cond_cases_continents].groupby("country")["weekly_count"].sum()
    continents_deaths = world_data[cond_deaths_continents].groupby("country")["weekly_count"].sum()
    new_df = pd.merge(continents_cases,continents_deaths,on="country",how="inner")
    new_df.rename(columns={'weekly_count_x': 'cases'}, inplace=True)
    new_df.rename(columns={'weekly_count_y': 'deaths'}, inplace=True)
    new_df["IFR"] = new_df["deaths"].div(new_df["cases"].values)
    continents = {
       "code": ['AF','AM','AS','EU','OC'],
       "cases": new_df["cases"].to_list(),
       "deaths": new_df["deaths"].to_list(),
       "IFR": new_df["IFR"].to_list()
    }
    continents_df = pd.DataFrame.from_dict(continents)
    
    if period == 'before':
        continents_df.to_csv('continents_covid(2020).csv',index=False)
    elif period == 'after':
        continents_df.to_csv('continents_covid(2021-2022).csv',index=False)
     
#Continents stats before vaccinations   
create_continents_csv(world_data,"before")
#Continents stats after vaccinations 
create_continents_csv(world_data,"after")