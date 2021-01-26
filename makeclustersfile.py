import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def makeclustersfile(filename):
    numclusters = 100
    df = pd.read_csv(filename)
    latlng = df[['metadata.lat','metadata.lng']]
    X = latlng.to_numpy()
    if len(X) > numclusters:
        kmeans = KMeans(numclusters)
        y_pred = kmeans.fit_predict(X)
        _, counts = np.unique(y_pred, return_counts=True)
        df = pd.DataFrame(kmeans.cluster_centers_, columns=['longitude','latitude'])
    else:
        df = pd.DataFrame(X, columns=['longitude','latitude'])
        counts = np.ones(len(latlng))
    df['counts'] = counts
    return df.to_json()
    