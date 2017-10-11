# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudImageSummaryLinks(Model):
    """CloudImageSummaryLinks.

    :param snappable:
    :type snappable: :class:`Link <rubriklib_int.models.Link>`
    :param snapshot:
    :type snapshot: :class:`Link <rubriklib_int.models.Link>`
    :param location:
    :type location: :class:`Link <rubriklib_int.models.Link>`
    """

    _attribute_map = {
        'snappable': {'key': 'snappable', 'type': 'Link'},
        'snapshot': {'key': 'snapshot', 'type': 'Link'},
        'location': {'key': 'location', 'type': 'Link'},
    }

    def __init__(self, snappable=None, snapshot=None, location=None):
        self.snappable = snappable
        self.snapshot = snapshot
        self.location = location