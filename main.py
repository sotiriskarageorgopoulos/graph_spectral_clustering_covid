import pandas as pd
from do_graph_clustering import do_graph_clustering 

countries = pd.read_csv("./data/eu_countries.csv")["geoId"].to_numpy() #EU countries

#Cluster of countries according to cases and deaths before vaccinations

covid_stats_bef_vacc = pd.read_csv("./data/covid_19(2020).csv")[["cases","deaths","geoId"]]
covid_stats_bef_vacc.fillna(method="ffill",inplace=True)
do_graph_clustering(countries,covid_stats_bef_vacc,"Cluster of countries before vaccination")

#Cluster of countries according to cases and deaths after vaccinations

covid_stats_after_vacc = pd.read_csv("./data/covid_19(2021-2022).csv")[["cases","deaths","geoId"]]
covid_stats_after_vacc.fillna(method="ffill", inplace=True)
do_graph_clustering(countries,covid_stats_after_vacc,"Cluster of countries after vaccination")