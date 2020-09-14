from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base, ToDoItem

engine = create_engine("sqlite:///tasks.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()

for desc in ("прочитать книгу", "выучить django", "помыть посуду","поесть"):
    t = ToDoItem(desc)
    s.add(t)

s.commit()
