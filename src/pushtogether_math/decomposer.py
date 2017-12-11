from sklearn import decomposition

def pca_decompose(dataset, n=2):
    """
    Applies the PCA to reduce the dimensionality of the dataset
    """
    pca = decomposition.PCA(n_components=n)
    pca.fit(dataset)
    transformed_dataset = pca.transform(dataset)
    return transformed_dataset
