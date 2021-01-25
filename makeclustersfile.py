import pandas as pd
from sklearn.cluster import KMeans
from os.path import splitext, basename
import numpy as np

def makeclustersfile(filename):
    df = pd.read_csv(filename)
    latlng = df[['metadata.lat','metadata.lng']]
    X = latlng.to_numpy()
    kmeans = KMeans()
    y_pred = kmeans.fit_predict(X)
    _, counts = np.unique(y_pred, return_counts=True)
    df = pd.DataFrame(kmeans.cluster_centers_, columns=['longitude','latitude'])
    df['counts'] = counts
    return df.to_json()
    