# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.default_error import DefaultError  # noqa: E501
from swagger_server.models.default_message import DefaultMessage  # noqa: E501
from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.models.notification_list import NotificationList  # noqa: E501
from swagger_server.models.notification_update import NotificationUpdate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNotificationController(BaseTestCase):
    """NotificationController integration test stubs"""

    def test_notification_acknowledge(self):
        """Test case for notification_acknowledge

        
        """
        body = NotificationUpdate()
        response = self.client.open(
            '/api/v1.0/notification/{notificationId}'.format(notificationId='notificationId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notification_get(self):
        """Test case for notification_get

        
        """
        response = self.client.open(
            '/api/v1.0/notification/{notificationId}'.format(notificationId='notificationId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notification_list(self):
        """Test case for notification_list

        
        """
        query_string = [('next_id', 56)]
        response = self.client.open(
            '/api/v1.0/notification',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
