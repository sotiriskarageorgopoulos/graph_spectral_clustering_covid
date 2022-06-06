import networkx as nx
import pandas as pd 
import numpy as np
from sklearn.cluster import SpectralClustering
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from predict_k import predict_k
import warnings
warnings.filterwarnings("ignore")

def do_graph_clustering(countries:np.ndarray,covid_stats:pd.DataFrame,graph_title:str):
    graph = nx.Graph()
    g_structure = []
    for i in range(len(countries)):
        country_a_stats = covid_stats[covid_stats["geoId"] == countries[i]]
        for j in range(i,len(countries)):
            country_b_stats = covid_stats[covid_stats["geoId"] == countries[j]]
            if countries[i] == countries[j]:
                continue
            
            samples = len(country_a_stats["geoId"])
            if len(country_a_stats["geoId"]) > len(country_b_stats["geoId"]):
                samples = len(country_b_stats["geoId"])
            elif len(country_a_stats["geoId"]) < len(country_b_stats["geoId"]): 
                samples = len(country_a_stats["geoId"])
                
            country_b_stats.fillna(method="ffill", inplace=True)
            cases_country_a = country_a_stats["cases"][:samples]
            deaths_country_a = country_a_stats["deaths"][:samples]
            
            cases_country_b = country_b_stats["cases"][:samples]
            deaths_country_b = country_b_stats["deaths"][:samples]
            
            cases_corr,p_val_1 = pearsonr(cases_country_a,cases_country_b)
            deaths_corr,p_val_2 = pearsonr(deaths_country_a,deaths_country_b)
            
            # print(f"({cases_corr},{deaths_corr})")
            weight = (cases_corr + deaths_corr) / 2
            
            a_edge_b = (countries[i],countries[j],{"weight": weight})
            g_structure.append(a_edge_b)
        
    graph.add_edges_from(g_structure)

    for (u, v, wt) in graph.edges.data('weight'):
        print(f"({u}, {v}, {wt:.3})")
            
    affinity_matrix = nx.to_numpy_array(graph)
    k = predict_k(graph)
    sc = SpectralClustering(k, affinity='precomputed', random_state=42, n_init=100)
    sc.fit(affinity_matrix)
    classes = sc.labels_

    plt.title(graph_title)
    nx.draw(graph,pos=nx.drawing.layout.spring_layout(graph),with_labels=True,node_color=classes,node_size=700,font_color="grey")
    plt.show()