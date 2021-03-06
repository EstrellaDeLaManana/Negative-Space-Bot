from os import environ
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Debe especificar un archivo de base de datos.")

    conn_str_sqlite = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    conn_str = environ.get('DATABASE_URL', conn_str_sqlite)
    print(f'Conexión a la base de datos en {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
