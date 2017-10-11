# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IdStatus(Model):
    """IdStatus.

    :param id:
    :type id: str
    :param status:
    :type status: :class:`Status <rubriklib_int.models.Status>`
    """

    _validation = {
        'id': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'Status'},
    }

    def __init__(self, id, status):
        self.id = id
        self.status = status