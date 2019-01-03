# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AccountDefinition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, permission: str=None, tag: object=None, domains: List[str]=None, create_date: datetime=None, last_modification_date: datetime=None):  # noqa: E501
        """AccountDefinition - a model defined in Swagger

        :param name: The name of this AccountDefinition.  # noqa: E501
        :type name: str
        :param permission: The permission of this AccountDefinition.  # noqa: E501
        :type permission: str
        :param tag: The tag of this AccountDefinition.  # noqa: E501
        :type tag: object
        :param domains: The domains of this AccountDefinition.  # noqa: E501
        :type domains: List[str]
        :param create_date: The create_date of this AccountDefinition.  # noqa: E501
        :type create_date: datetime
        :param last_modification_date: The last_modification_date of this AccountDefinition.  # noqa: E501
        :type last_modification_date: datetime
        """
        self.swagger_types = {
            'name': str,
            'permission': str,
            'tag': object,
            'domains': List[str],
            'create_date': datetime,
            'last_modification_date': datetime
        }

        self.attribute_map = {
            'name': 'name',
            'permission': 'permission',
            'tag': 'tag',
            'domains': 'domains',
            'create_date': 'create_date',
            'last_modification_date': 'last_modification_date'
        }

        self._name = name
        self._permission = permission
        self._tag = tag
        self._domains = domains
        self._create_date = create_date
        self._last_modification_date = last_modification_date

    @classmethod
    def from_dict(cls, dikt) -> 'AccountDefinition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccountDefinition of this AccountDefinition.  # noqa: E501
        :rtype: AccountDefinition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this AccountDefinition.


        :return: The name of this AccountDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AccountDefinition.


        :param name: The name of this AccountDefinition.
        :type name: str
        """

        self._name = name

    @property
    def permission(self) -> str:
        """Gets the permission of this AccountDefinition.


        :return: The permission of this AccountDefinition.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission: str):
        """Sets the permission of this AccountDefinition.


        :param permission: The permission of this AccountDefinition.
        :type permission: str
        """
        allowed_values = ["Read", "Write", "AdminRead", "AdminWrite", "SelfRegisterDomain"]  # noqa: E501
        if permission not in allowed_values:
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def tag(self) -> object:
        """Gets the tag of this AccountDefinition.


        :return: The tag of this AccountDefinition.
        :rtype: object
        """
        return self._tag

    @tag.setter
    def tag(self, tag: object):
        """Sets the tag of this AccountDefinition.


        :param tag: The tag of this AccountDefinition.
        :type tag: object
        """

        self._tag = tag

    @property
    def domains(self) -> List[str]:
        """Gets the domains of this AccountDefinition.


        :return: The domains of this AccountDefinition.
        :rtype: List[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains: List[str]):
        """Sets the domains of this AccountDefinition.


        :param domains: The domains of this AccountDefinition.
        :type domains: List[str]
        """

        self._domains = domains

    @property
    def create_date(self) -> datetime:
        """Gets the create_date of this AccountDefinition.


        :return: The create_date of this AccountDefinition.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date: datetime):
        """Sets the create_date of this AccountDefinition.


        :param create_date: The create_date of this AccountDefinition.
        :type create_date: datetime
        """

        self._create_date = create_date

    @property
    def last_modification_date(self) -> datetime:
        """Gets the last_modification_date of this AccountDefinition.


        :return: The last_modification_date of this AccountDefinition.
        :rtype: datetime
        """
        return self._last_modification_date

    @last_modification_date.setter
    def last_modification_date(self, last_modification_date: datetime):
        """Sets the last_modification_date of this AccountDefinition.


        :param last_modification_date: The last_modification_date of this AccountDefinition.
        :type last_modification_date: datetime
        """

        self._last_modification_date = last_modification_date