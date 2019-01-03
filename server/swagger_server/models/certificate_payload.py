# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CertificatePayload(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, certification: str=None, key: str=None, ca: str=None):  # noqa: E501
        """CertificatePayload - a model defined in Swagger

        :param certification: The certification of this CertificatePayload.  # noqa: E501
        :type certification: str
        :param key: The key of this CertificatePayload.  # noqa: E501
        :type key: str
        :param ca: The ca of this CertificatePayload.  # noqa: E501
        :type ca: str
        """
        self.swagger_types = {
            'certification': str,
            'key': str,
            'ca': str
        }

        self.attribute_map = {
            'certification': 'certification',
            'key': 'key',
            'ca': 'ca'
        }

        self._certification = certification
        self._key = key
        self._ca = ca

    @classmethod
    def from_dict(cls, dikt) -> 'CertificatePayload':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CertificatePayload of this CertificatePayload.  # noqa: E501
        :rtype: CertificatePayload
        """
        return util.deserialize_model(dikt, cls)

    @property
    def certification(self) -> str:
        """Gets the certification of this CertificatePayload.


        :return: The certification of this CertificatePayload.
        :rtype: str
        """
        return self._certification

    @certification.setter
    def certification(self, certification: str):
        """Sets the certification of this CertificatePayload.


        :param certification: The certification of this CertificatePayload.
        :type certification: str
        """

        self._certification = certification

    @property
    def key(self) -> str:
        """Gets the key of this CertificatePayload.


        :return: The key of this CertificatePayload.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this CertificatePayload.


        :param key: The key of this CertificatePayload.
        :type key: str
        """

        self._key = key

    @property
    def ca(self) -> str:
        """Gets the ca of this CertificatePayload.


        :return: The ca of this CertificatePayload.
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca: str):
        """Sets the ca of this CertificatePayload.


        :param ca: The ca of this CertificatePayload.
        :type ca: str
        """

        self._ca = ca