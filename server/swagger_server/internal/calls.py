import builtins
import datetime
from db import *

from swagger_server.models.default_error import DefaultError
from swagger_server.models.default_message import DefaultMessage
from swagger_server.models.account_definition import AccountDefinition
from swagger_server.models.account_definition_list import AccountDefinitionList

PAGING_SIZE = 30

def _render_account(db_account):
    tags = {}
    for tag in db_account.tags:
        tags[tag.key] = tag.value
    return AccountDefinition(
        name=db_account.name,
        permission=db_account.permission,
        tag=tags,
        domains=db_account.domains,
        create_date=db_account.creation_date,
        last_modification_date=db_account.last_modification_date,
    )

def _account_create(body):
    session = builtins.CAS_CONTEXT['db_session']()
    name = body.name
    permission = body.permission

    try:
        new_account = Account(
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
        return DefaultError(code='InvalidInputData', message=log_msg), 400

    if body.tag is not None:
        for tag in body.tag:
            tag = TagAccount(key=tag, value=body.tag[tag], account_id=new_account.id)
            session.add(tag)

    session.commit()
    session.refresh(new_account)

    ret = _render_account(new_account)
    session.close()
    return ret 

def _account_delete(accountId):
    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(Account).filter_by(name=accountId).first()
    # TODO handle cascading or error messages when certificates/domains/notifications are
    # still present 
    if account is not None:
        for tag in account.tags:
            session.delete(tag)
        session.query(Account).filter_by(name=accountId).delete()
        log_msg = "user '%s' deleted" % accountId
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        ret = DefaultMessage(message=log_msg)
        ret_code = 200
    else:
        log_msg = "user '%s' doesn't exist, nothing to be done" % accountId
        builtins.CAS_CONTEXT['logger'].info(log_msg)
        ret = DefaultError(message=log_msg)
        ret_code = 404

    session.commit()
    session.close()
    return ret , ret_code

def _account_get(accountId):
    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(Account).filter_by(name=accountId).first()
    if account is None:
        log_msg = "user '%s' doesn't exist" % accountId
        session.close()
        return DefaultError(message=log_msg), 404
    ret = _render_account(account)
    session.close()
    if ret is None:
        log_msg = 'Account "%s" doesn\'t exist' % accountId
        builtins.CAS_CONTEXT['logger'].warning(log_msg)
        return DefaultError(code='InvalidInputData', message=log_msg), 404
    return ret

def _account_list(next_id=None):
    if next_id is None:
        next_id = 0
    session = builtins.CAS_CONTEXT['db_session']()
    accounts = session.query(Account).filter(Account.id > next_id).order_by(Account.id).limit(PAGING_SIZE)
    rendered_accounts = []
    for account in accounts:
        rendered_accounts.append(_render_account(account))
    if len(rendered_accounts) == PAGING_SIZE:
        next_id = account.id
    elif len(rendered_accounts) == 0:
        next_id = None
    else:
        next_id = None
    ret = AccountDefinitionList()
    ret.list = rendered_accounts
    ret.next_id = next_id
    session.close()
    return ret

def _account_update(accountId, body):
    session = builtins.CAS_CONTEXT['db_session']()
    account = session.query(Account).filter_by(name=accountId).first()
    if account is None:
        log_msg = "user '%s' doesn't exist" % accountId
        return DefaultError(message=log_msg), 404
    if body.name:
        account.name = body.name
    if body.permission:
        account.permission = body.permission
    if account.tags is not None:
        for tag in account.tags:
            session.delete(tag)
    account.last_modification_date = datetime.datetime.now()
    for tag in body.tag:
        tag = TagAccount(key=tag, value=body.tag[tag], account_id=account.id)
        session.add(tag)
    session.commit()
    session.refresh(account)
    ret = _render_account(account)
    session.close()
    return ret

def _apikey_create(accountId):
    pass

def _apikey_delete(accountId, keyId):
    pass

def _apikey_get(accountId, keyId):
    pass

def _apikey_list(accountId, next_id=None):
    pass

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
