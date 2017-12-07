from sklearn import decomposition

def decompose(dataset, n=2):
    pca = decomposition.PCA(n_components=n)
    pca.fit(dataset)
    transformed_dataset = pca.transform(dataset)
    return transformed_dataset
