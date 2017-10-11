# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PrincipalSearchRequest(Model):
    """PrincipalSearchRequest.

    :param limit: Maximum number of results to return
    :type limit: int
    :param offset: Starting offset of the results to return
    :type offset: int
    :param queries: List of search queries to perform
    :type queries: list of :class:`PrincipalQuery
     <rubriklib_int.models.PrincipalQuery>`
    :param sort: List of fields by which to sort the result set
    :type sort: list of :class:`PrincipalSort
     <rubriklib_int.models.PrincipalSort>`
    """

    _validation = {
        'limit': {'minimum': 0},
        'offset': {'minimum': 0},
        'queries': {'required': True},
    }

    _attribute_map = {
        'limit': {'key': 'limit', 'type': 'int'},
        'offset': {'key': 'offset', 'type': 'int'},
        'queries': {'key': 'queries', 'type': '[PrincipalQuery]'},
        'sort': {'key': 'sort', 'type': '[PrincipalSort]'},
    }

    def __init__(self, queries, limit=None, offset=None, sort=None):
        self.limit = limit
        self.offset = offset
        self.queries = queries
        self.sort = sort