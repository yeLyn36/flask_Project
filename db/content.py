# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from .base import Base
from datetime import datetime


class diary(Base):
    __tablename__ = 'diary'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    create_date = Column(datetime)
    update_date = Column(datetime)

    def __init__(self, id, title, content, create_date, update_date):
        self.id = id
        self.title = title
        self.content = content
        self.create_date = create_date
        self.update_date = update_date

    def __repr__(self):
        return ("< Diary number: %d\n  title: %s\n  content: %s\n  create_date:%s\n  update_date:%s>" % (self.id, self.title, self.content, self.create_date, self.update_date))

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "create_date": self.create_date,
            "update_date": self.update_date
        }