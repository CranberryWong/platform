#! /usr/bin/env python
#coding:utf-8

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from settings import DBSETTINGS
from datetime import datetime

Base = declarative_base()

class Article(Base):
   __tablename__ = 'article'

   aid = Column(Integer, primary_key=True)
   atitle = Column(String(35))
   acontent = Column(Text)
   acreatetime = Column(DateTime, nullable=False)
   amodifytime = Column(DateTime, nullable=False)
   acid = Column(Integer, ForeignKey('category.cid'))
   acheck = Column(Boolean)


   acate = relationship('Category', backref='category')

   def __init__(self, atitle, acontent, acid):
      self.atitle = atitle
      self.acontent = acontent
      self.acreatetime = datetime.now()
      self.amodifytime = datetime.now()
      self.acheck = True
      self.acid = acid

   def __repr__(self):
      return "<Article('%s')>" % (self.atitle)

class Category(Base):
    __tablename__ = 'category'

    cid = Column(Integer, primary_key=True)
    cname = Column(String(100))
    ccheck = Column(Boolean)

    cateofa = relationship('Article')

    def __init__(self, cname):
        self.cname = cname
        self.ccheck = True

    def __repr__(self):
        return "<Category('%s')>" % (self.cname)

class Setting(Base):
    __tablename__ = 'setting'

    sid = Column(Integer, primary_key=True)
    sname = Column(String(100), nullable=False)
    sadmin = Column(String(100), nullable=False)
    spwd = Column(String(100), nullable=False)
    scount = Column(Integer)

    def __init__(self, sname, sadmin, spwd):
        self.sname = sname
        self.sadmin = sadmin
        self.spwd = spwd
        self.scount = 0

    def __repr__(self):
        return "<Setting('%s')>" % (self.sname)

class Link(Base):
    __tablename__ = "link"

    lid = Column(Integer, primary_key=True)
    lname = Column(String(100), nullable=False)
    lurl = Column(String(200), nullable=False)

    def __init__(self):
        self.lname = lname
        self.lurl = lurl

    def __repr__(self):
        return "<Link('%s')>" % (self.lname)

def getDBURL():
   return 'mysql+mysqlconnector://%s:%s@%s:%d/%s' % (DBSETTINGS['db_user'], DBSETTINGS['db_password'], DBSETTINGS['db_host'], DBSETTINGS['db_port'], DBSETTINGS['db_name'])

class DB_Session(object):
    def __init__(self):
        engine = create_engine(getDBURL())
        self.Session = sessionmaker(bind=engine)

    @property
    def getSession(self):
        return self.Session()

db_session = DB_Session()
