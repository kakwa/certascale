import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String

from sqlalchemy.types import DateTime, Boolean, LargeBinary

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


from version import DB_VERSION, VERSION

DB_VERSION_LABEL = 'DB_VERSION'
VERSION_LABEL = 'VERSION'
Base = declarative_base()

class DbSchemaTooNew(Exception):
    pass

class DbNoVersionSet(Exception):
    pass

def migrate():
    """Place holder for futur DB migration scripts"""
    pass

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    tags = relationship("TagAccount")
    name = Column(String(30), unique=True)
    permission = Column(String(30))
    creation_date = Column(DateTime())
    last_modification_date = Column(DateTime())
    api_keys = relationship("ApiKey")
    domains = relationship("Domain")
    notifications = relationship("Notification")


class ApiKey(Base):
    __tablename__ = 'api_key'
    id = Column(Integer, primary_key=True)
    secrete = Column(String(256))
    creation_date = Column(DateTime())
    last_modification_date = Column(DateTime())
    account_id = Column(Integer, ForeignKey('account.id'))


class Domain(Base):
    __tablename__ = 'domain'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    creation_date = Column(DateTime())
    last_modification_date = Column(DateTime())
    account_id = Column(Integer, ForeignKey('account.id'))
    notifications = relationship("Notification")
    tags = relationship("TagDomain")


class Certificate(Base):
    __tablename__ = 'certificate'
    id = Column(Integer, primary_key=True)
    valid_start = Column(DateTime())
    valid_end = Column(DateTime())
    latest_valid = Column(Boolean())
    name = Column(String(256))
    ca_name = Column(String(256))
    public_key = Column(LargeBinary())
    private_key = Column(LargeBinary())
    account_id = Column(Integer, ForeignKey('account.id'))
    domain_id = Column(Integer, ForeignKey('domain.id'))


class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    message = Column(String(256))
    payload = Column(String(256))
    status = Column(String(256))
    status_message = Column(String(256))
    domain_id = Column(Integer, ForeignKey('domain.id'))
    account_id = Column(Integer, ForeignKey('account.id'))


class TagAccount(Base):
    __tablename__ = 'tagaccount'
    id = Column(Integer, primary_key=True)
    key = Column(String(30))
    value = Column(String(30))
    account_id = Column(Integer, ForeignKey('account.id'))


class TagDomain(Base):
    __tablename__ = 'tagdomain'
    id = Column(Integer, primary_key=True)
    key = Column(String(30))
    value = Column(String(256))
    account_id = Column(Integer, ForeignKey('domain.id'))


class Version(Base):
    __tablename__ = 'version'
    id = Column(Integer, primary_key=True)
    version = Column(String(10))
    vtype = Column(String(10), nullable=False, unique=True)


def get_dbpool(config):

    engine = create_engine(
            config['uri'],
            echo=(config['echo_sql'] in ['true', 'True', 'TRUE']),
#            pool_size = int(config['pool_size']),
#            pool_timeout = int(config['pool_timeout']),
#            pool_recycle = int(config['pool_recycle'])
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # we try to get the version, if it doesn't succeed, we create the DB
    try:
        version = session.query(Version).filter_by(vtype=DB_VERSION_LABEL).first()
    except (sqlalchemy.exc.OperationalError, sqlalchemy.exc.ProgrammingError):
        Base.metadata.create_all(engine)
        # committing between schema creation and
        # setting the version is necessary on postgres
        session.commit()
        # we set the version
        while True:
            try:
                session.add_all([
                    Version(vtype = DB_VERSION_LABEL, version = DB_VERSION),
                    Version(vtype = VERSION_LABEL, version = VERSION),
                ])
                session.commit()
                version = session.query(Version).filter_by(vtype=DB_VERSION_LABEL).first()
                break
            except:
                pass

    # the version of the DB is newer than the version of certascale
    # this should not happen so we raise an exception
    if version is None:
        raise DbNoVersionSet
    if int(version.version) > int(DB_VERSION):
        raise DbSchemaTooNew

    # the version of the DB is older than the certascale definition
    # so we launch the schema update script
    elif int(version.version) < int(DB_VERSION):
        migrate()
