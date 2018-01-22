import pytest

from pushtogether_math import cluster

class TestCluster:

    def test_cluster_users_on_the_same_cluster(self, votes):
        """
        These users should be clustered in the same group
        """
        response = cluster.get_clusters(votes)
        assert response[1]['group'] == response[2]['group']
        assert response[3]['group'] == response[4]['group']
    
    def test_cluster_users_on_different_clusters(self, votes):
        """
        These users should be clustered in different groups
        """
        response = cluster.get_clusters(votes)
        assert response[1]['group'] != response[3]['group']
        assert response[2]['group'] != response[4]['group']
