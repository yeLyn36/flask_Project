#-*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .base import Base
from datetime import datetime

class content(Base):
    __tablename__ = 'content'

    id = Column(String(100), primary_key=True)
    title = Column(String(100), unique=True)
    content = Column(String(10000000))
    date = Column(datetime)


    def __init__(self, id, title, content, date):
        self.id = id
        self.title = title
        self.content = content
        self.date = date


    def __repr__(self):
        return (self.id + self.title + self.content + self.date)

    @property
    def serialize(self):
       return {
           "id": self.id,
           "title": self.title,
           "content": self.content,
           "date": self.date,
       }
        