import pandas as pd
from do_graph_clustering import do_graph_clustering 

countries = pd.read_csv("./data/eu_countries.csv")["geoId"].to_numpy() #EU countries

#Cluster of countries according to cases and deaths before vaccinations

covid_stats_bef_vacc = pd.read_csv("./data/covid_19(2020).csv")
covid_stats_bef_vacc.fillna(method="ffill",inplace=True)
norm_df_bef_vacc = (covid_stats_bef_vacc[['cases','deaths']]-covid_stats_bef_vacc[['cases','deaths']].mean())/(covid_stats_bef_vacc[['cases','deaths']].max()-covid_stats_bef_vacc[['cases','deaths']].min())
covid_stats_bef_vacc.loc[:,['cases','deaths']] = norm_df_bef_vacc[['cases','deaths']]
do_graph_clustering(covid_stats_bef_vacc,"Cluster of countries before vaccination")

#Cluster of countries according to cases and deaths after vaccinations

covid_stats_after_vacc = pd.read_csv("./data/covid_19(2021-2022).csv")
covid_stats_after_vacc.fillna(method="ffill", inplace=True)
cols_after_vacc = ["FirstDose","SecondDose","DoseAdditional1","DoseAdditional2","cases","deaths"]
norm_df_bef_vacc = (covid_stats_after_vacc[cols_after_vacc]-covid_stats_after_vacc[cols_after_vacc].mean())/(covid_stats_after_vacc[cols_after_vacc].max()-covid_stats_after_vacc[cols_after_vacc].min())
covid_stats_after_vacc.loc[:,cols_after_vacc] = norm_df_bef_vacc[cols_after_vacc]
do_graph_clustering(covid_stats_after_vacc,"Cluster of countries after vaccination")