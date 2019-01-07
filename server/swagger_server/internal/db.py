import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from version import DB_VERSION, VERSION

DB_VERSION_LABEL = 'DB_VERSION'
VERSION_LABEL = 'VERSION'
Base = declarative_base()

class DbSchemaTooNew(Exception):
    pass

def migrate():
    """Place holder for futur DB migration scripts"""
    pass

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)

class Key(Base):
    __tablename__ = 'key'
    id = Column(Integer, primary_key=True)

class Domain(Base):
    __tablename__ = 'domain'
    id = Column(Integer, primary_key=True)

class Certificate(Base):
    __tablename__ = 'certificate'
    id = Column(Integer, primary_key=True)

class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)

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
    except sqlalchemy.exc.OperationalError:
        Base.metadata.create_all(engine)
        # we set the version
        session.add_all([
            Version(vtype = DB_VERSION_LABEL, version = DB_VERSION),
            Version(vtype = VERSION_LABEL, version = VERSION),
        ])
        session.commit()
        version = session.query(Version).filter_by(vtype=DB_VERSION_LABEL).first()

    # the version of the DB is newer than the version of certascale
    # this should not happen so we raise an exception
    if int(version.version) > int(DB_VERSION):
        raise DbSchemaTooNew

    # the version of the DB is older than the certascale definition
    # so we launch the schema update script
    elif int(version.version) < int(DB_VERSION):
        migrate()
