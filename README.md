SQLAlchemy-ModelID provides a base for [SQLAlchemy](https://www.sqlalchemy.org/) models with a `model_id` property. This conveniently distinguishes between models with the same primary key but from different tables.

## Installation

```
$ pip install sqlalchemy-modelid
```

## Quickstart

```python
from sqlalchemy_modelid import ModelIdBase

# standard session creation
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///:memory:')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()
Base = declarative_base()

# subclass `ModelIdBase` to add a `model_id` property to any model
class Model(ModelIdBase, Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)

# create the database
Base.metadata.create_all(engine)

# example
my_model = Model()
session.add(my_model)
session.commit()
my_model.model_id
```

Out:

```
model-1
```

## Citation

```
@software{bowen2020sqlalchemy-modelid,
  author = {Dillon Bowen},
  title = {SQLAlchemy-ModelID},
  url = {https://dsbowen.github.io/sqlalchemy-modelid/},
  date = {2020-06-05},
}
```

## License

Users must cite this package in any publications which use it.

It is licensed with the MIT [License](https://github.com/dsbowen/sqlalchemy-modelid/blob/master/LICENSE).