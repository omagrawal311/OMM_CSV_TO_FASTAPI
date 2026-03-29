from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/school_db"

engine=create_engine(DATABASE_URL,pool_pre_ping=True)

Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()