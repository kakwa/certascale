import connexion
import six

from swagger_server.models.account_create_update import AccountCreateUpdate  # noqa: E501
from swagger_server.models.account_definition import AccountDefinition  # noqa: E501
from swagger_server.models.account_definition_list import AccountDefinitionList  # noqa: E501
from swagger_server.models.api_key import ApiKey  # noqa: E501
from swagger_server.models.api_key_list import ApiKeyList  # noqa: E501
from swagger_server.models.default_error import DefaultError  # noqa: E501
from swagger_server.models.default_message import DefaultMessage  # noqa: E501
from swagger_server import util


import swagger_server.internal.calls as calls

import builtins

def account_create(body):  # noqa: E501
    """account_create

    Create a new account # noqa: E501

    :param body: Data structure to create the account
    :type body: dict | bytes

    :rtype: AccountDefinition
    """
    if connexion.request.is_json:
        body = AccountCreateUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return calls._account_create(body)


def account_delete(accountId):  # noqa: E501
    """account_delete

    Remove the account # noqa: E501

    :param accountId:
    :type accountId: str

    :rtype: DefaultMessage
    """
    return calls._account_delete(accountId)


def account_get(accountId):  # noqa: E501
    """account_get

    Get the details of a specific account # noqa: E501

    :param accountId:
    :type accountId: str

    :rtype: AccountDefinition
    """
    return calls._account_get(accountId)


def account_list(next_id=None):  # noqa: E501
    """account_list

    Get the list of accounts (paginated) # noqa: E501

    :param next_id:
    :type next_id: int

    :rtype: AccountDefinitionList
    """
    return calls._account_list(next_id)


def account_update(accountId, body):  # noqa: E501
    """account_update

    Update an existing account # noqa: E501

    :param accountId:
    :type accountId: str
    :param body:
    :type body: dict | bytes

    :rtype: DefaultMessage
    """
    if connexion.request.is_json:
        body = AccountCreateUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return calls._account_update(accountId, body)


def apikey_create(accountId):  # noqa: E501
    """apikey_create

    Create a new API key # noqa: E501

    :param accountId:
    :type accountId: str

    :rtype: ApiKey
    """
    return calls._apikey_create(accountId)


def apikey_delete(accountId, keyId):  # noqa: E501
    """apikey_delete

    Delete a given key # noqa: E501

    :param accountId:
    :type accountId: str
    :param keyId:
    :type keyId: str

    :rtype: DefaultMessage
    """
    return calls._apikey_delete(accountId, keyId)


def apikey_get(accountId, keyId):  # noqa: E501
    """apikey_get

    Get a given API key # noqa: E501

    :param accountId:
    :type accountId: str
    :param keyId:
    :type keyId: str

    :rtype: ApiKey
    """
    return calls._apikey_get(accountId, keyId)


def apikey_list(accountId, next_id=None):  # noqa: E501
    """apikey_list

    Get the list of API keys for a given account # noqa: E501

    :param accountId:
    :type accountId: str
    :param next_id:
    :type next_id: int

    :rtype: ApiKeyList
    """
    return calls._apikey_list(accountId, next_id)
