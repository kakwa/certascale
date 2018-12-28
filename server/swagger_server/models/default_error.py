# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DefaultError(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None):  # noqa: E501
        """DefaultError - a model defined in Swagger

        :param code: The code of this DefaultError.  # noqa: E501
        :type code: str
        :param message: The message of this DefaultError.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'code': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'DefaultError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DefaultError of this DefaultError.  # noqa: E501
        :rtype: DefaultError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this DefaultError.

        Error code  # noqa: E501

        :return: The code of this DefaultError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this DefaultError.

        Error code  # noqa: E501

        :param code: The code of this DefaultError.
        :type code: str
        """
        allowed_values = ["AccessDeny", "InsufficientPermission", "InvalidInputData"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this DefaultError.

        Error message details  # noqa: E501

        :return: The message of this DefaultError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this DefaultError.

        Error message details  # noqa: E501

        :param message: The message of this DefaultError.
        :type message: str
        """

        self._message = message
