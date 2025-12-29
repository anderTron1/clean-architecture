from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.base import Base

from src.infra.db.entities.users import Users # pylint: disable=unused-import

def create_tables():
    db = DBConnectionHandler()
    engine = db.get_engine()
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print(">> Tabelas criadas com sucesso")