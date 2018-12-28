import connexion
import six

from swagger_server.models.default_error import DefaultError  # noqa: E501
from swagger_server.models.default_message import DefaultMessage  # noqa: E501
from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.models.notification_list import NotificationList  # noqa: E501
from swagger_server.models.notification_update import NotificationUpdate  # noqa: E501
from swagger_server import util


def notification_acknowledge(notificationId, body):  # noqa: E501
    """notification_acknowledge

    Acknowledge the notification # noqa: E501

    :param notificationId: 
    :type notificationId: str
    :param body: 
    :type body: dict | bytes

    :rtype: DefaultMessage
    """
    if connexion.request.is_json:
        body = NotificationUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def notification_get(notificationId):  # noqa: E501
    """notification_get

    Get specific content for a notification # noqa: E501

    :param notificationId: 
    :type notificationId: str

    :rtype: Notification
    """
    return 'do some magic!'


def notification_list(next_id=None):  # noqa: E501
    """notification_list

    Get all your certificate update notifications # noqa: E501

    :param next_id: 
    :type next_id: int

    :rtype: NotificationList
    """
    return 'do some magic!'
