import connexion
import six

from swagger_server.models.certificate import Certificate  # noqa: E501
from swagger_server.models.certificate_list import CertificateList  # noqa: E501
from swagger_server.models.certificate_payload import CertificatePayload  # noqa: E501
from swagger_server.models.default_error import DefaultError  # noqa: E501
from swagger_server.models.default_message import DefaultMessage  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.domain_create_update import DomainCreateUpdate  # noqa: E501
from swagger_server.models.domain_list import DomainList  # noqa: E501
from swagger_server import util


def certificate_create(domainName, body):  # noqa: E501
    """certificate_create

    Post an externally generated certificate # noqa: E501

    :param domainName: 
    :type domainName: str
    :param body: 
    :type body: dict | bytes

    :rtype: DefaultMessage
    """
    if connexion.request.is_json:
        body = CertificatePayload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def certificate_delete(domainName, certificateId):  # noqa: E501
    """certificate_delete

    Remove the certificate # noqa: E501

    :param domainName: 
    :type domainName: str
    :param certificateId: 
    :type certificateId: str

    :rtype: DefaultMessage
    """
    return 'do some magic!'


def certificate_get(domainName, certificateId):  # noqa: E501
    """certificate_get

    Get a specific certificate and the associated key and CA # noqa: E501

    :param domainName: 
    :type domainName: str
    :param certificateId: 
    :type certificateId: str

    :rtype: Certificate
    """
    return 'do some magic!'


def certificate_list(domainName, next_id=None):  # noqa: E501
    """certificate_list

    Get the list of certificate for a specific domain # noqa: E501

    :param domainName: 
    :type domainName: str
    :param next_id: 
    :type next_id: int

    :rtype: CertificateList
    """
    return 'do some magic!'


def domain_create(body):  # noqa: E501
    """domain_create

    Register a new domain # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Domain
    """
    if connexion.request.is_json:
        body = DomainCreateUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def domain_delete(domainName):  # noqa: E501
    """domain_delete

    Remove the domain # noqa: E501

    :param domainName: 
    :type domainName: str

    :rtype: DefaultMessage
    """
    return 'do some magic!'


def domain_get(domainName):  # noqa: E501
    """domain_get

    Get the details of a specific domain # noqa: E501

    :param domainName: 
    :type domainName: str

    :rtype: Domain
    """
    return 'do some magic!'


def domain_list(next_id=None):  # noqa: E501
    """domain_list

    Get the list of your domains # noqa: E501

    :param next_id: 
    :type next_id: int

    :rtype: DomainList
    """
    return 'do some magic!'
