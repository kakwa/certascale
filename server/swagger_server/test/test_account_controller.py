# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.account_create_update import AccountCreateUpdate  # noqa: E501
from swagger_server.models.account_definition import AccountDefinition  # noqa: E501
from swagger_server.models.account_definition_list import AccountDefinitionList  # noqa: E501
from swagger_server.models.api_key import ApiKey  # noqa: E501
from swagger_server.models.api_key_list import ApiKeyList  # noqa: E501
from swagger_server.models.default_error import DefaultError  # noqa: E501
from swagger_server.models.default_message import DefaultMessage  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccountController(BaseTestCase):
    """AccountController integration test stubs"""

    def test_account_create(self):
        """Test case for account_create

        
        """
        body = AccountCreateUpdate()
        response = self.client.open(
            '/api/v1.0/account',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_delete(self):
        """Test case for account_delete

        
        """
        response = self.client.open(
            '/api/v1.0/account/{accountId}'.format(accountId='accountId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_get(self):
        """Test case for account_get

        
        """
        response = self.client.open(
            '/api/v1.0/account/{accountId}'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_list(self):
        """Test case for account_list

        
        """
        query_string = [('next_id', 56)]
        response = self.client.open(
            '/api/v1.0/account',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_account_update(self):
        """Test case for account_update

        
        """
        body = AccountCreateUpdate()
        response = self.client.open(
            '/api/v1.0/account/{accountId}'.format(accountId='accountId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apikey_create(self):
        """Test case for apikey_create

        
        """
        response = self.client.open(
            '/api/v1.0/account/{accountId}/apikey/'.format(accountId='accountId_example'),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apikey_delete(self):
        """Test case for apikey_delete

        
        """
        response = self.client.open(
            '/api/v1.0/account/{accountId}/apikey/{keyId}'.format(accountId='accountId_example', keyId='keyId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apikey_get(self):
        """Test case for apikey_get

        
        """
        response = self.client.open(
            '/api/v1.0/account/{accountId}/apikey/{keyId}'.format(accountId='accountId_example', keyId='keyId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apikey_list(self):
        """Test case for apikey_list

        
        """
        query_string = [('next_id', 56)]
        response = self.client.open(
            '/api/v1.0/account/{accountId}/apikey/'.format(accountId='accountId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
