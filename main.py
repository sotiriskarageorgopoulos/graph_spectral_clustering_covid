import pandas as pd
from do_graph_clustering import do_graph_clustering 

#Cluster of countries according to cases, deaths and IFR before vaccinations in EU

covid_stats_bef_eu = pd.read_csv("./data/eu_covid_19(2020).csv")
norm_df_bef_eu = (covid_stats_bef_eu[['cases','deaths']]-covid_stats_bef_eu[['cases','deaths']].mean())/(covid_stats_bef_eu[['cases','deaths']].max()-covid_stats_bef_eu[['cases','deaths']].min())
covid_stats_bef_eu.loc[:,['cases','deaths']] = norm_df_bef_eu[['cases','deaths']]
do_graph_clustering(covid_stats_bef_eu,"Cluster of countries before vaccination in European Union")

#Cluster of countries according to cases, deaths, IFR, FirstDose, SecondDose, DoseAdditional1 and DoseAdditional1 after vaccinations in EU

covid_stats_after_eu = pd.read_csv("./data/eu_covid_19(2021-2022).csv")
cols_after_eu = ["FirstDose","SecondDose","DoseAdditional1","DoseAdditional2","cases","deaths","IFR"]
norm_df_after_eu = (covid_stats_after_eu[cols_after_eu]-covid_stats_after_eu[cols_after_eu].mean())/(covid_stats_after_eu[cols_after_eu].max()-covid_stats_after_eu[cols_after_eu].min())
covid_stats_after_eu.loc[:,cols_after_eu] = norm_df_after_eu[cols_after_eu]
do_graph_clustering(covid_stats_after_eu,"Cluster of countries after vaccination in European Union")

#Cluster of countries according to cases, deaths and IFR before vaccinations in Europe

covid_stats_before_europe = pd.read_csv("./data/europe_continent_covid(2020).csv")
norm_df_bef_europe = (covid_stats_before_europe[['cases','deaths']]-covid_stats_before_europe[['cases','deaths']].mean())/(covid_stats_before_europe[['cases','deaths']].max()-covid_stats_before_europe[['cases','deaths']].min())
covid_stats_before_europe.loc[:,['cases','deaths']] = norm_df_bef_europe[['cases','deaths']]
do_graph_clustering(covid_stats_before_europe,"Cluster of countries before vaccination in Europe")

#Cluster of countries according to cases, deaths and IFR before vaccinations in Europe

covid_stats_after_europe = pd.read_csv("./data/europe_continent_covid(2021-2022).csv")
norm_df_after_europe = (covid_stats_after_europe[['cases','deaths']]-covid_stats_after_europe[['cases','deaths']].mean())/(covid_stats_after_europe[['cases','deaths']].max()-covid_stats_after_europe[['cases','deaths']].min())
covid_stats_after_europe.loc[:,['cases','deaths']] = norm_df_after_europe[['cases','deaths']]
do_graph_clustering(covid_stats_after_europe,"Cluster of countries after vaccination in Europe")

#Cluster of countries according to cases, deaths and IFR before vaccinations in Asia

covid_stats_before_asia = pd.read_csv("./data/asia_continent_covid(2020).csv")
norm_df_bef_asia = (covid_stats_before_asia[['cases','deaths']]-covid_stats_before_asia[['cases','deaths']].mean())/(covid_stats_before_asia[['cases','deaths']].max()-covid_stats_before_asia[['cases','deaths']].min())
covid_stats_before_asia.loc[:,['cases','deaths']] = norm_df_bef_asia[['cases','deaths']]
do_graph_clustering(covid_stats_before_asia,"Cluster of countries before vaccination in Asia")

#Cluster of countries according to cases, deaths and IFR before vaccinations in Asia

covid_stats_after_asia = pd.read_csv("./data/asia_continent_covid(2021-2022).csv")
norm_df_after_asia = (covid_stats_after_asia[['cases','deaths']]-covid_stats_after_asia[['cases','deaths']].mean())/(covid_stats_after_asia[['cases','deaths']].max()-covid_stats_after_asia[['cases','deaths']].min())
covid_stats_after_asia.loc[:,['cases','deaths']] = norm_df_after_asia[['cases','deaths']]
do_graph_clustering(covid_stats_after_asia,"Cluster of countries after vaccination in Asia")

#Cluster of countries according to cases, deaths and IFR before vaccinations in Oceania

covid_stats_before_oceania = pd.read_csv("./data/oceania_continent_covid(2020).csv")
norm_df_bef_oceania = (covid_stats_before_oceania[['cases','deaths']]-covid_stats_before_oceania[['cases','deaths']].mean())/(covid_stats_before_oceania[['cases','deaths']].max()-covid_stats_before_oceania[['cases','deaths']].min())
covid_stats_before_oceania.loc[:,['cases','deaths']] = norm_df_bef_oceania[['cases','deaths']]
do_graph_clustering(covid_stats_before_oceania,"Cluster of countries before vaccination in Oceania")

#Cluster of countries according to cases, deaths and IFR before vaccinations in Oceania

covid_stats_after_oceania = pd.read_csv("./data/oceania_continent_covid(2021-2022).csv")
norm_df_after_oceania = (covid_stats_after_oceania[['cases','deaths']]-covid_stats_after_oceania[['cases','deaths']].mean())/(covid_stats_after_oceania[['cases','deaths']].max()-covid_stats_after_oceania[['cases','deaths']].min())
covid_stats_after_oceania.loc[:,['cases','deaths']] = norm_df_after_oceania[['cases','deaths']]
do_graph_clustering(covid_stats_after_oceania,"Cluster of countries after vaccination in Oceania")

#Cluster of countries according to cases, deaths and IFR before vaccinations in America
covid_stats_before_america = pd.read_csv("./data/america_continent_covid(2020).csv")
norm_df_bef_america = (covid_stats_before_america[['cases','deaths']]-covid_stats_before_america[['cases','deaths']].mean())/(covid_stats_before_america[['cases','deaths']].max()-covid_stats_before_america[['cases','deaths']].min())
covid_stats_before_america.loc[:,['cases','deaths']] = norm_df_bef_america[['cases','deaths']]
do_graph_clustering(covid_stats_before_america,"Cluster of countries before vaccination in America")

#Cluster of countries according to cases, deaths and IFR after vaccinations in America
covid_stats_after_america = pd.read_csv("./data/america_continent_covid(2021-2022).csv")
norm_df_after_america = (covid_stats_after_america[['cases','deaths']]-covid_stats_after_america[['cases','deaths']].mean())/(covid_stats_after_america[['cases','deaths']].max()-covid_stats_after_america[['cases','deaths']].min())
covid_stats_after_america.loc[:,['cases','deaths']] = norm_df_after_america[['cases','deaths']]
do_graph_clustering(covid_stats_after_america,"Cluster of countries after vaccination in America")

#Cluster of continents according to cases, deaths and IFR before vaccinations
covid_stats_before_continents = pd.read_csv("./data/continents_covid(2020).csv")
norm_df_bef_continents = (covid_stats_before_continents[['cases','deaths']]-covid_stats_before_continents[['cases','deaths']].mean())/(covid_stats_before_continents[['cases','deaths']].max()-covid_stats_before_continents[['cases','deaths']].min())
covid_stats_before_continents.loc[:,['cases','deaths']] = norm_df_bef_continents[['cases','deaths']]
do_graph_clustering(covid_stats_before_continents,"Cluster of continents before vaccination")

#Cluster of contitents according to cases, deaths and IFR after vaccinations
covid_stats_after_continents = pd.read_csv("./data/continents_covid(2021-2022).csv")
norm_df_after_continents = (covid_stats_after_continents[['cases','deaths']]-covid_stats_after_continents[['cases','deaths']].mean())/(covid_stats_after_continents[['cases','deaths']].max()-covid_stats_after_continents[['cases','deaths']].min())
covid_stats_after_continents.loc[:,['cases','deaths']] = norm_df_after_continents[['cases','deaths']]
do_graph_clustering(covid_stats_after_continents,"Cluster of continents after vaccination")