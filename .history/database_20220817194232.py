from sqlalchemy import create_engine
from sqlalchemy.orm  import  declarative_base, sessionmaker

engine=create_engine('postgresql://postgres:space@localhost/pizzaapi',
  echo=True
)

Base=declarative_base()

Session=sessionMaker()