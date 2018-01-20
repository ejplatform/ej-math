import pytest

from src.pushtogether_math import cluster

class TestCluster:

    def test_cluster_users_on_the_same_cluster(self, votes):
        response = cluster.get_clusters(votes)
        assert response[1]['group'] == response[2]['group']
        assert response[3]['group'] == response[4]['group']
    
    def test_cluster_users_on_different_clusters(self, votes):
        response = cluster.get_clusters(votes)
        assert response[1]['group'] != response[3]['group']
        assert response[2]['group'] != response[4]['group']
