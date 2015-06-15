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

class Pagination(object):
    def __init__(self):
        self.pre = ''
        self.next = ''
        self.pages = []
        self.current = ''
        self.action = ''

def generatePagination(action, bloglist, targetpage):
    targetpage = int(targetpage)
    pagination = Pagination()
    pagination.current = targetpage
    maxpage = len(bloglist)
    pagination.pages = range(1, maxpage/10+2)
    pagination.pre = str(targetpage-1) if targetpage-1 in pagination.pages else str(targetpage)
    pagination.next = str(targetpage+1) if targetpage+1 in pagination.pages else str(targetpage)
    pagination.action = action
    bloglist = bloglist[(targetpage-1) * 10 : targetpage * 10]
    return bloglist, pagination

class homeBase(SignValidateBase):
    def init(self):
        self.session = db_session.getSession
        self.thisquery = None
        self.setting = self.session.query(Setting).all()
        self.categoryList = self.session.query(Category).filter(Category.cname != '上市公司景气指数').filter(Category.cname != '上市公司质量评价').filter(Category.ccheck == True).all()
        setting = self.session.query(Setting).filter(Setting.sid == 1).first()
        setting.scount += 1
        self.session.commit()
        self.count = setting.scount

class staticBase(homeBase):
    def init(self, cid):
        homeBase.init(self)
        #所有类型
        self.links = self.session.query(Link).all()
        #归档
        articlelist = self.session.query(Article).filter(Article.acid == cid).order_by(Article.acreatetime.desc()).all()
        topyear = articlelist[0].acreatetime.year
        bottomyear = articlelist[len(articlelist) - 1].acreatetime.year
        self.articlebydate = []
        for year in range(bottomyear, topyear + 1):
            for month in range(1, 13):
                nums = len([article for article in articlelist if article.acreatetime.year == year and article.acreatetime.month ==month])
                if nums != 0:
                    self.articlebydate.insert(0, {'year':year, 'month':month, 'num':nums})

class Home(homeBase):
    def get(self):
        homeBase.init(self)
        self.title = 'Home'
        article = self.session.query(Article).filter(Article.aid == 1).first()
        self.render('home_index.html', article = article)
        self.session.close()

class showArticle(staticBase):
    def get(self, cid, aid):
        staticBase.init(self, cid)
        article = self.session.query(Article).filter(Article.aid == aid).first()
        self.title = article.atitle
        self.render('home_page.html', article = article, cid = cid)
        self.session.close()

class showList(staticBase):
    def get(self, cid):
        staticBase.init(self, cid)
        List = self.session.query(Category).filter(Category.cid == cid).first().cateofa
        category = self.session.query(Category).filter(Category.cid == cid).first()
        self.title = category.cname
        targetpage = int(self.get_argument('page',default='1'))
        articleList, self.pagination = generatePagination('/c/'+cid+'?page=', List, targetpage)
        self.render('home_list.html', articleList = articleList, cid = cid)
        self.session.close()

class showAbout(homeBase):
    def get(self):
        homeBase.init(self)
        self.title = 'About us'
        info_path = os.path.join(self.get_template_path(), 'aboutme.md')
        aboutcontent = markdown.markdown(open(info_path).read().decode('utf8'))
        self.render('home_about.html', aboutcontent = aboutcontent)
        self.session.close()

class listByDate(staticBase):
    def get(self,year,month,cid):
        staticBase.init(self,cid)
        targetpage = int(self.get_argument('page',default='1'))
        articlelist = [article for article in self.session.query(Article).filter(Article.acid == cid).all() if article.acreatetime.year == int(year) and article.acreatetime.month == int(month)]
        list, self.pagination = generatePagination('/date/' + year + '/' + month + '/c/' + cid +'?page=', articlelist, targetpage)
        self.thisquery = "归档：" + str(year) + "年" + str(month) + "月"
        self.title = "归档：" + str(year) + "年" + str(month) + "月"
        self.render("home_list.html", list = list)
        self.session.close()
