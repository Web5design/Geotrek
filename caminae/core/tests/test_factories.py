from django.test import TestCase

from .. import factories


class CoreFactoriesTest(TestCase):
    """
    Ensure factories work as expected.
    Here we just call each one to ensure they do not trigger any random
    error without verifying any other expectation.
    """

    def test_path_factory(self):
        factories.PathFactory()

    def test_topology_mixin_factory(self):
        factories.TopologyMixinFactory()

    def test_topology_mixin_kind_factory(self):
        factories.TopologyMixinKindFactory()

    def test_path_aggregation_factory(self):
        factories.PathAggregationFactory()

    def test_datasource_management_factory(self):
        factories.DatasourceManagementFactory()

    def test_challenge_management_factory(self):
        factories.ChallengeManagementFactory()

    def test_usage_management_factory(self):
        factories.UsageManagementFactory()

    def test_network_management_factory(self):
        factories.NetworkManagementFactory()

    def test_path_management_factory(self):
        factories.PathManagementFactory()
