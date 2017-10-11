# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FailureToleranceStatus(Model):
    """FailureToleranceStatus.

    :param brik: Number of brik failures allowed in the cluster under which
     the cluster remains fully functional
    :type brik: int
    :param node: Number of node failures allowed in the cluster under which
     the cluster remains fully functional
    :type node: int
    :param disk: Number of disk failures allowed in the cluster under which
     the cluster remains fully functional
    :type disk: int
    """

    _validation = {
        'brik': {'required': True},
        'node': {'required': True},
        'disk': {'required': True},
    }

    _attribute_map = {
        'brik': {'key': 'brik', 'type': 'int'},
        'node': {'key': 'node', 'type': 'int'},
        'disk': {'key': 'disk', 'type': 'int'},
    }

    def __init__(self, brik, node, disk):
        self.brik = brik
        self.node = node
        self.disk = disk