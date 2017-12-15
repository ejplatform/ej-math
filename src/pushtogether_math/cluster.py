from . import kmeans

def get_clusters(votes):
    """
    Receives vote stream input that should be a list with the following format
    [('choice', 'user_id', 'comment_id'), ...]
    """
    return kmeans.make_clusters(votes)
