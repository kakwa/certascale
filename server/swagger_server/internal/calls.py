import builtins
import datetime
import hashlib
import secrets
from db import *

from swagger_server.models.default_error import DefaultError as swg_DefaultError
from swagger_server.models.default_message import DefaultMessage as swg_DefaultMessage
from swagger_server.models.account_definition import AccountDefinition as swg_AccountDefinition
from swagger_server.models.account_definition_list import AccountDefinitionList as swg_AccountDefinitionList
from swagger_server.models.api_key import ApiKey as swg_ApiKey

from flask import request

PAGING_SIZE = 30

MAX_KEY_PER_ACCOUNT = 10

AUTH_HEADER_NAME = 'X-API-KEY'

def _render_account(db_account):
    tags = {}
    for tag in db_account.tags:
        tags[tag.key] = tag.value
    return swg_AccountDefinition(
        name=db_account.name,
        permission=db_account.permission,
        tag=tags,
        domains=db_account.domains,
        create_date=db_account.creation_date,
        last_modification_date=db_account.last_modification_date,
    )


def _access_deny(api_msg='access deny, invalid/missing API key',
        log_msg='access deny, invalid/missing API key'):
    builtins.CAS_CONTEXT['logger'].info(log_msg)
    return swg_DefaultError(code='AccessDeny', message=api_msg), 403


def _insuf_perm(api_msg='access deny, invalid/missing API key',
        log_msg='access deny, invalid/missing API key'):
    builtins.CAS_CONTEXT['logger'].info(log_msg)
    return swg_DefaultError(code='InsufficientPermission', message=api_msg), 403


def access_control():
    api_key = request.headers.get(AUTH_HEADER_NAME)
    if api_key is None:
        return None
    secret_hash = hashlib.sha512(api_key.encode('utf-8')).hexdigest()
    session = builtins.CAS_CONTEXT['db_session']()
    key = session.query(DbApiKey).filter_by(secret_hash=secret_hash).first()
    if key is not None:
        return {'id': key.account.id,
                'perm': key.account.permission,
                'name': key.account.name
        }
    else:
        return None


def _check_perm(account, allowed_roles, action, checked_id=None,
                api_msg="access deny, not enough permission",
                log_msg="access deny, not enough permission for user '%s' to do '%s'"):
    if account is None:
        return _access_deny(), 403

    if account['perm'] not in allowed_roles \
        or (checked_id and checked_id != account['name']):
        return _insuf_perm(
                    log_msg=log_msg % (account['name'], action),
                    api_msg=api_msg,
                ), 403
    return None


def _account_create(body):
    account =  access_control()
    perm = _check_perm(account, ['AdminWrite'], 'create account')
    if perm:
        return perm

    session = builtins.CAS_CONTEXT['db_session']()
    name = body.name
    permission = body.permission

    try:
        new_account = DbAccount(
                name=name,
                permission=permission,
                creation_date=datetime.datetime.now(),
                last_modification_date=datetime.datetime.now()
        )
        session.add(new_account)
        session.flush()
        session.refresh(new_account)

    except sqlalchemy.exc.IntegrityError as e:
        # loss matching of not unique account name
        if 'unique' not in str(e) or 'UNIQUE' not in str(e):
            log_msg = 'Duplicate account name, account "%s" already exists' % name
        else:
            log_msg = 'Invalid/incomplete data in the payload'
        #log_msg = str(e)
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        return swg_DefaultError(code='InvalidInputData', message=log_msg), 400

    if body.tag is not None:
        for tag in body.tag:
            tag = DbTagAccount(key=tag, value=body.tag[tag], account_id=new_account.id)
            session.add(tag)

    session.commit()
    session.refresh(new_account)

    ret = _render_account(new_account)
    session.close()
    return ret 


def _account_delete(accountId):
    account =  access_control()

    if account is None:
        return _access_deny(log_msg="access deny on account delete")

    if account['perm'] not in ['AdminWrite']:
        return _access_deny(
                log_msg="user '%s' (perm: %s) doesn't have permission to delete an account" % (account['name'], account['perm']),
                api_msg="deleting an account requires admin permission",
                )
    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(DbAccount).filter_by(name=accountId).first()
    # TODO handle cascading or error messages when certificates/domains/notifications are
    # still present 
    if account is not None:
        for tag in account.tags:
            session.delete(tag)
        session.query(DbAccount).filter_by(name=accountId).delete()
        log_msg = "user '%s' deleted" % accountId
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        ret = swg_DefaultMessage(message=log_msg)
        ret_code = 200
    else:
        log_msg = "user '%s' doesn't exist, nothing to be done" % accountId
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        ret = swg_DefaultError(message=log_msg)
        ret_code = 404

    session.commit()
    session.close()
    return ret , ret_code


def _account_get(accountId):
    if account is None:
        return _access_deny(log_msg="access deny on account delete")
    if account['perm'] in ['AdminWrite', 'AdminRead'] or \
        account['name'] != accountId and account['perm'] in ['Read', 'Write', 'SelfRegisterDomain']:
        return _access_deny(
                log_msg="user '%s' (perm: %s) doesn't have permission to read an account" % (account['name'], account['perm']),
                api_msg="read an account requires admin (read) permission",
                )

    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(DbAccount).filter_by(name=accountId).first()
    if account is None:
        log_msg = "user '%s' doesn't exist" % accountId
        session.close()
        return swg_DefaultError(message=log_msg), 404
    ret = _render_account(account)
    session.close()
    if ret is None:
        log_msg = 'Account "%s" doesn\'t exist' % accountId
        builtins.CAS_CONTEXT['logger'].warning(log_msg)
        return swg_DefaultError(code='InvalidInputData', message=log_msg), 404
    return ret

def _account_list(next_id=None):
    if next_id is None:
        next_id = 0
    session = builtins.CAS_CONTEXT['db_session']()
    accounts = session.query(DbAccount).filter(DbAccount.id > next_id).order_by(DbAccount.id).limit(PAGING_SIZE)
    rendered_accounts = []
    for account in accounts:
        rendered_accounts.append(_render_account(account))
    if len(rendered_accounts) == PAGING_SIZE:
        next_id = account.id
    elif len(rendered_accounts) == 0:
        next_id = None
    else:
        next_id = None
    ret = swg_AccountDefinitionList()
    ret.list = rendered_accounts
    ret.next_id = next_id
    session.close()
    return ret

def _account_update(accountId, body):
    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(DbAccount).filter_by(name=accountId).first()
    if account is None:
        log_msg = "user '%s' doesn't exist" % accountId
        return swg_DefaultError(message=log_msg), 404
    if body.name:
        account.name = body.name
    if body.permission:
        account.permission = body.permission
    if account.tags is not None:
        for tag in account.tags:
            session.delete(tag)
    account.last_modification_date = datetime.datetime.now()
    for tag in body.tag:
        tag = DbTagAccount(key=tag, value=body.tag[tag], account_id=account.id)
        session.add(tag)
    session.commit()
    session.refresh(account)
    ret = _render_account(account)
    session.close()
    return ret

def _render_apikey(key, fullkey=None):
    ret = swg_ApiKey()
    if fullkey is not None:
        ret.secret = fullkey
    else:
        ret.secret = "%s-XXXXXXX" % key.secret_prefix
    ret.create_date = key.creation_date
    ret.id = key.id
    ret.last_modification_date = key.last_modification_date
    return ret

def _apikey_create(accountId):
    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(DbAccount).filter_by(name=accountId).first()
    if account is None:
        log_msg = "user '%s' doesn't exist" % accountId
        session.close()
        return swg_DefaultError(message=log_msg), 404

    if len(account.api_keys) > MAX_KEY_PER_ACCOUNT:
        log_msg = "user '%s' already has the maximum number of keys (%d)" % (accountId, MAX_KEY_PER_ACCOUNT)
        session.close()
        return swg_DefaultError(message=log_msg), 401

    secret_prefix = secrets.token_hex(4)
    secret_main = secrets.token_urlsafe(32)
    api_key = "%s-%s" % (secret_prefix, secret_main)
    hashed_key = hashlib.sha512(api_key.encode('utf-8')).hexdigest()
    dbapi_key = DbApiKey(secret_hash=hashed_key,
           creation_date=datetime.datetime.now(),
           secret_prefix=secret_prefix,
           account_id=account.id,
           )
    session.add(dbapi_key)
    session.commit()
    ret = _render_apikey(dbapi_key, fullkey=api_key)
    session.close()
    return ret

def _apikey_delete(accountId, keyId):
    session = builtins.CAS_CONTEXT['db_session']()
    # TODO: join in one query instead of two queries...
    try:
        internal_account_id = session.query(DbAccount).filter_by(name=accountId).first().id
    except:
        log_msg = "cannot delete key, user '%s' doesn't exist" % accountId
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        session.close()
        return swg_DefaultError(code='InvalidInputData', message=log_msg), 404
    key = session.query(DbApiKey).filter_by(id=keyId, account_id=internal_account_id).first()
    if key is not None:
        log_msg = "key '%s' (key: '%s-XXXX') of user '%s' deleted" % (keyId, key.secret_prefix, accountId)
        ret = swg_DefaultMessage(message=log_msg)
        ret_code = 200
        session.delete(key)
        session.commit()
    else:
        log_msg = "cannot delete, key '%s' of user '%s' doesn't exist" % (keyId, accountId)
        ret_code = 404
        ret = swg_DefaultError(code='InvalidInputData', message=log_msg)
    builtins.CAS_CONTEXT['logger'].info(log_msg)
    session.close()
    return ret, ret_code

def _apikey_get(accountId, keyId):
    session = builtins.CAS_CONTEXT['db_session']()
    # TODO: join in one query instead of two queries...
    try:
        internal_account_id = session.query(DbAccount).filter_by(name=accountId).first().id
    except:
        log_msg = "cannot delete key, user '%s' doesn't exist" % accountId
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        session.close()
        return swg_DefaultError(code='InvalidInputData', message=log_msg), 404
    key = session.query(DbApiKey).filter_by(id=keyId, account_id=internal_account_id).first()
    if key is None:
        ret_code = 404
        log_msg = "key '%s' of user '%s' doesn't exist" % (keyId, accountId)
        ret = swg_DefaultError(code='InvalidInputData', message=log_msg)
    else:
        ret_code = 200
        ret = _render_apikey(key)
        log_msg = "key '%s' of user '%s' queried" % (keyId, accountId)
    builtins.CAS_CONTEXT['logger'].info(log_msg)
    return ret, ret_code

def _apikey_list(accountId, next_id=None):
    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(DbAccount).filter_by(name=accountId).first()
    if account is None:
        log_msg = "cannot list keys, user '%s' doesn't exist" % accountId
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        session.close()
        return swg_DefaultError(code='InvalidInputData', message=log_msg), 404
    ret = []
    for k in account.api_keys:
        ret.append(_render_apikey(k))
    return ret

def _certificate_create(domainName, body):
    pass

def _certificate_delete(domainName, certificateId):
    pass

def _certificate_get(domainName, certificateId):
    pass

def _certificate_list(domainName, next_id=None):
    pass

def _domain_create(body):
    pass

def _domain_delete(domainName):
    pass

def _domain_get(domainName):
    pass

def _domain_list(next_id=None):
    pass

def _notification_acknowledge(notificationId, body):
    pass

def _notification_get(notificationId):
    pass

def _notification_list(next_id=None):
    pass
