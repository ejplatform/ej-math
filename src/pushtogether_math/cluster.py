import pandas as pd
from sklearn.cluster import KMeans

from . import decomposer
from . import data_converter

def get_labels(data, n_clusters=2):
    """
    Receives a Numpy Array and applies sklearn KMeans clustering algorithm to
    return the labels with respective user's groups
    """
    kmeans = KMeans(n_clusters=n_clusters)
    clustered_data = kmeans.fit(data)
    labels = clustered_data.labels_

    return labels

def create_cluster_info_dataframe(votes, pca_votes, users_labels):
    """
    Generates a Pandas DataFrame with the clustering information.
    Returns the X, Y and group_id values
    """
    dataframe = pd.DataFrame(pca_votes, index=votes.index, columns=['x','y'])
    grouped_dataframe = dataframe.assign(group=users_labels)

    return grouped_dataframe

def make_clusters(votes):
    """
    Converts the vote list in a Pandas DataFrame that passes through a PCA
    dimensionality reduction and then through a KMeans clustering algorithm.
    The result is an Pandas DataFrame containing each user's group info.

    Vote stream input should be a list with the following format
    [('choice', 'user_id', 'comment_id'), ...]
    """
    votes_dataframe = data_converter.convert_to_dataframe(votes)
    pca_votes = decomposer.pca_decompose(votes_dataframe.values)
    users_labels = get_labels(pca_votes)
    grouped_users_info = create_cluster_info_dataframe(votes_dataframe, pca_votes, users_labels)

    return grouped_users_info
