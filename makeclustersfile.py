import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def makeclustersfile(filename):
    numclusters = 100
    df = pd.read_csv(filename)
    latlng = df[['metadata.lng','metadata.lat']]
    X = latlng.to_numpy()
    if len(X) > numclusters:
        kmeans = KMeans(numclusters)
        y_pred = kmeans.fit_predict(X)
        _, count = np.unique(y_pred, return_counts=True)
        df = pd.DataFrame(kmeans.cluster_centers_, columns=['lng','lat'])
    else:
        df = pd.DataFrame(X, columns=['lng','lat'])
        count = np.ones(len(latlng))
    df['count'] = count
    return df.to_json(orient='records')
