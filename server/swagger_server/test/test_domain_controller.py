# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.certificate import Certificate  # noqa: E501
from swagger_server.models.certificate_list import CertificateList  # noqa: E501
from swagger_server.models.certificate_payload import CertificatePayload  # noqa: E501
from swagger_server.models.default_error import DefaultError  # noqa: E501
from swagger_server.models.default_message import DefaultMessage  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.domain_create_update import DomainCreateUpdate  # noqa: E501
from swagger_server.models.domain_list import DomainList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDomainController(BaseTestCase):
    """DomainController integration test stubs"""

    def test_certificate_create(self):
        """Test case for certificate_create

        
        """
        body = CertificatePayload()
        response = self.client.open(
            '/api/v1.0/domain/{domainName}/certificate/'.format(domainName='domainName_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_certificate_delete(self):
        """Test case for certificate_delete

        
        """
        response = self.client.open(
            '/api/v1.0/domain/{domainName}/certificate/{certificateId}'.format(domainName='domainName_example', certificateId='certificateId_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_certificate_get(self):
        """Test case for certificate_get

        
        """
        response = self.client.open(
            '/api/v1.0/domain/{domainName}/certificate/{certificateId}'.format(domainName='domainName_example', certificateId='certificateId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_certificate_list(self):
        """Test case for certificate_list

        
        """
        query_string = [('next_id', 56)]
        response = self.client.open(
            '/api/v1.0/domain/{domainName}/certificate/'.format(domainName='domainName_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_create(self):
        """Test case for domain_create

        
        """
        body = DomainCreateUpdate()
        response = self.client.open(
            '/api/v1.0/domain',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_delete(self):
        """Test case for domain_delete

        
        """
        response = self.client.open(
            '/api/v1.0/domain/{domainName}'.format(domainName='domainName_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_get(self):
        """Test case for domain_get

        
        """
        response = self.client.open(
            '/api/v1.0/domain/{domainName}'.format(domainName='domainName_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domain_list(self):
        """Test case for domain_list

        
        """
        query_string = [('next_id', 56)]
        response = self.client.open(
            '/api/v1.0/domain',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
