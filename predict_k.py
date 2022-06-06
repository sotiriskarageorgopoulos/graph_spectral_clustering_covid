import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def predict_k(graph):
    e =  nx.normalized_laplacian_spectrum(graph,weight="weight")
    eigenvalues = 1 - e
    dk = abs(np.diff(eigenvalues))
    position = np.argmax(dk)
    k = position + 2
    plt.title("Eigenvalues for different k.")
    plt.plot(np.arange(1,len(e)+1),eigenvalues)
    plt.show()
    return k