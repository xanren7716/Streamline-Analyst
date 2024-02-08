import streamlit as st
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering, SpectralClustering
from sklearn.mixture import GaussianMixture

@st.cache_data
def train_select_cluster_model(X_train, n, model_type, model_params=None):
    if model_type == 1:
        return KMeans_train(X_train, n, model_params)
    elif model_type == 2:
        return DBSCAN_train(X_train, model_params)
    elif model_type == 3:
        return GaussianMixture_train(X_train, n, model_params)
    elif model_type == 4:
        return Hierarchical_train(X_train, n, model_params)
    elif model_type == 5:
        return Spectral_train(X_train, n, model_params)

def KMeans_train(X_train, n_clusters=3, model_params=None):
    if model_params is None: model_params = {}
    kmeans = KMeans(n_clusters=n_clusters, **model_params)
    kmeans.fit(X_train)
    return kmeans

def DBSCAN_train(X_train, model_params=None):
    if model_params is None: model_params = {}
    dbscan = DBSCAN(**model_params)
    dbscan.fit(X_train)
    return dbscan

def GaussianMixture_train(X_train, n_components=1, model_params=None):
    if model_params is None: model_params = {}
    gmm = GaussianMixture(n_components=n_components, **model_params)
    gmm.fit(X_train)
    return gmm

def Hierarchical_train(X_train, n_clusters=3, model_params=None):
    if model_params is None: model_params = {}
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters, **model_params)
    hierarchical.fit(X_train)
    return hierarchical

def Spectral_train(X_train, n_clusters=3, model_params=None):
    if model_params is None: model_params = {}
    spectral = SpectralClustering(n_clusters=n_clusters, **model_params)
    spectral.fit(X_train)
    return spectral