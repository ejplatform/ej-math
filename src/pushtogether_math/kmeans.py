import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from . import decomposer
from . import data_converter


def get_labels(data, n_clusters=2):
    """
    Receives a Numpy Array and applies sklearn KMeans clustering algorithm to
    return the labels with respective user's groups
    """
    kmeans = KMeans(n_clusters=n_clusters, max_iter=300, verbose=0, random_state=0)
    labels = kmeans.fit_predict(data)

    return labels


def get_labels_with_max_silhouette(data, n_clusters_range):
    """
    Receives a Numpy Array and applies sklearn KMeans clustering algorithm
    to a range of numbers of clusters and calculates the silhouette value
    for each one, then returns the KMeans labels with the max silhouette
    """
    first_n_clusters, *rest_n_clusters = n_clusters_range
    silhouette = None
    best_labels = get_labels(data, first_n_clusters)
    for n_clusters in rest_n_clusters:
        labels = get_labels(data, n_clusters)
        if set(labels) > 1:
            current_silhouette = silhouette_score(data, labels)
            if silhouette is None or current_silhouette > silhouette:
                silhouette = current_silhouette
                best_labels = labels

    return best_labels


def create_cluster_info_dataframe(votes, pca_votes, users_labels):
    """
    Generates a Pandas DataFrame with the clustering information.
    Returns the X, Y and group_id values
    """
    dataframe = pd.DataFrame(pca_votes, index=votes.index, columns=['x', 'y'])
    grouped_dataframe = dataframe.assign(group=users_labels.labels_)

    return grouped_dataframe


def make_clusters(votes, n_clusters_range):
    """
    Converts the vote list in a Pandas DataFrame that passes through a PCA
    dimensionality reduction and then through a KMeans clustering algorithm.
    The result is an Pandas DataFrame containing each user's group info.

    Vote stream input should be a list with the following format
    [('choice', 'user_id', 'comment_id'), ...]
    """
    votes_dataframe = data_converter.convert_to_dataframe(votes)
    pca_votes = decomposer.pca_decompose(votes_dataframe.values)
    users_labels = get_labels_with_max_silhouette(pca_votes, n_clusters_range)
    grouped_users_info = create_cluster_info_dataframe(
        votes_dataframe, pca_votes, users_labels)

    return grouped_users_info.T.to_dict()
