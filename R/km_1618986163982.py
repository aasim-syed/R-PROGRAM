# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 05:44:08 2021

@author: AmuthaVasan
"""
from pandas import DataFrame
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics

X=[[1,1],[2,2],[2,3],[1,4],[3,3],[6,7],[7,8],[6,8],[7,6],[6,9],[2,5],[7,8],[8,9],[6,7],[7,8],[3,1],[8,4],[8,6],[8,9]]
for k in range(2,6):
    kmeans = KMeans(n_clusters=k)
    kmeans = kmeans.fit(X)
    labels = kmeans.predict(X)
    centroids = kmeans.cluster_centers_
    print(labels)
    print(centroids)
    c = ['b','r','y','g','c','m']
    colors = [c[i] for i in labels]
    #plt.scatter(X[:,0],X[:,1], c=colors, s=18)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=100, c='black')
    silhouette_samples = metrics.silhouette_samples(X, kmeans.labels_)
    print(silhouette_samples)
    print("Average of Silhouette Coefficients for k =", k)
    print("============================================")
    print("Silhouette mean:", silhouette_samples.mean())