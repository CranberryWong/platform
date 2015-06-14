#! /usr/bin/env python
#coding=utf-8

import logging
import time
import os
import tornado.web
import markdown
import random
from models.entity import Article, Category, Setting, Link
from models.entity import db_session
from handler.admin import SignValidateBase
from datetime import datetime
from PIL import Image
from cStringIO import StringIO

picture_path = os.path.join(os.path.abspath('.'), 'static/picture/')

class homeBase(SignValidateBase):
    def init(self):
        self.session = db_session.getSession
        self.setting = self.session.query(Setting).all()
        category = self.session.query(Category).filter(Category.ccheck == True).all()
        setting = self.session.query(Setting).filter(Setting.sid == 1).first()
        setting.scount += 1
        self.session.commit()
        self.count = setting.scount

class Home(homeBase):
    def get(self):
        homeBase.init(self)
        self.title = 'Home'
        categoryList = self.session.query(Category).filter(Category.ccheck == True).all()
        article = self.session.query(Article).filter(Article.aid == 1).first()
        self.render('home.html', categoryList = categoryList, article = article)
        self.session.close()

class showArticle(homeBase):
    def get(self, aid):
        homeBase.init(self)
        self.title = 'Home'
        categoryList = self.session.query(Category).filter(Category.ccheck == True).all()
        article = self.session.query(Article).filter(Article.aid == aid).first()
        self.title = article.atitle
        self.render('home.html', article = article, categoryList = categoryList)
        self.session.close()
