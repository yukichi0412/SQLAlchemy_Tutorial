from sqlalchemy import Column, Integer, String, DateTime, Sequence
from datetime import datetime

from config.db import Base, create_engine, make_session

class Category():
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    created_at = Column('created', DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return self.title
