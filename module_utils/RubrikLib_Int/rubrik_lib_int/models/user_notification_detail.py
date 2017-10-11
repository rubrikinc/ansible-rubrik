# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserNotificationDetail(Model):
    """UserNotificationDetail.

    :param notification_id:
    :type notification_id: str
    :param name:
    :type name: str
    :param notification_type:
    :type notification_type: str
    :param notification_status:
    :type notification_status: str
    :param object_type:
    :type object_type: str
    :param object_id:
    :type object_id: str
    :param object_name:
    :type object_name: str
    :param notification_timestamp:
    :type notification_timestamp: long
    :param notification_info:
    :type notification_info: str
    :param state:
    :type state: str
    """

    _validation = {
        'notification_id': {'required': True},
        'name': {'required': True},
        'notification_type': {'required': True},
        'notification_status': {'required': True},
        'object_type': {'required': True},
        'object_id': {'required': True},
        'notification_timestamp': {'required': True},
        'notification_info': {'required': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'notification_id': {'key': 'notificationId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'notification_type': {'key': 'notificationType', 'type': 'str'},
        'notification_status': {'key': 'notificationStatus', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_name': {'key': 'objectName', 'type': 'str'},
        'notification_timestamp': {'key': 'notificationTimestamp', 'type': 'long'},
        'notification_info': {'key': 'notificationInfo', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, notification_id, name, notification_type, notification_status, object_type, object_id, notification_timestamp, notification_info, state, object_name=None):
        self.notification_id = notification_id
        self.name = name
        self.notification_type = notification_type
        self.notification_status = notification_status
        self.object_type = object_type
        self.object_id = object_id
        self.object_name = object_name
        self.notification_timestamp = notification_timestamp
        self.notification_info = notification_info
        self.state = state