import networkx as nx
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from predict_k import predict_k
from gaussian_similarity import gaussian_similarity_kernel
import warnings
warnings.filterwarnings("ignore")

def do_graph_clustering(covid_stats:pd.DataFrame,graph_title:str):
    countries =  covid_stats.to_numpy()
    graph = nx.Graph()
    g_structure = []
    for i in range(len(countries)):
        for j in range(i,len(countries)):
            if countries[i][0] == countries[j][0]:
                continue
            
            weight = gaussian_similarity_kernel(countries[i][1:],countries[j][1:],1)
            a_edge_b = (countries[i][0],countries[j][0],{"weight": weight})
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