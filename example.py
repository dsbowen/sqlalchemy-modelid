"""SQLAlchemy-ModelId example"""

"""Setup"""
# 1. Import ModelIdBase
from sqlalchemy_modelid import ModelIdBase

# 2. Standard session creation
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///:memory:')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()
Base = declarative_base()

# 3. Subclass `ModelIdBase` to add a `model_id` property to any model
class Model(ModelIdBase, Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)

# 4. Create the database
Base.metadata.create_all(engine)

"""Example"""

my_model = Model()
session.add(my_model)
session.commit()
print(my_model.model_id)