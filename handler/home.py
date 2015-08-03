#! /usr/bin/env python
#coding=utf-8

import logging
import time
import os
import tornado.web
import random
import tornado.locale
from models.entity import Article, Category, Setting, Link
from models.entity import db_session
from handler.admin import SignValidateBase, Pagination, generatePagination, picture_path
from datetime import datetime
from PIL import Image
from cStringIO import StringIO

global lang_encode
lang_encode = 'zh_CN'
tornado.locale.set_default_locale(lang_encode)

class changeLang(tornado.web.RequestHandler):
    def get(self):
        global lang_encode
        if lang_encode == 'zh_CN':
            lang_encode = 'en_US'
        else:
            lang_encode = 'zh_CN'
        tornado.locale.set_default_locale(lang_encode)
        self.redirect('/')

class homeBase(SignValidateBase):
    def init(self):
        self.session = db_session.getSession
        self.thisquery = None
        self.setting = self.session.query(Setting).all()
		#lizhuang改了
        self.categoryList = self.session.query(Category).filter(Category.ccheck == True).order_by(Category.serial).all()
        setting = self.session.query(Setting).filter(Setting.sid == 1).first()
        setting.scount += 1
        global lang_encode
        print lang_encode
        if lang_encode == 'zh_CN':
            self.lang = 'English'
        else:
            self.lang = '中文版'
        self.session.commit()
        self.count = setting.scount

    def get_user_locale(self):
        #return tornado.locale.set_default_locale('en_US')
        return tornado.locale.get("en_US")

class staticBase(homeBase):
    def init(self, cid):
        homeBase.init(self)
        #所有类型
        self.links = self.session.query(Link).all()
        #归档
        articlelist = self.session.query(Article).filter(Article.acid == cid).order_by(Article.acreatetime.desc()).all()
        if len(articlelist) != 0:
            topyear = articlelist[0].acreatetime.year
            bottomyear = articlelist[len(articlelist) - 1].acreatetime.year
            self.articlebydate = []
            for year in range(bottomyear, topyear + 1):
                for month in range(1, 13):
                    nums = len([article for article in articlelist if article.acreatetime.year == year and article.acreatetime.month ==month])
                    if nums != 0:
                        self.articlebydate.insert(0, {'year':year, 'month':month, 'num':nums})
        else:
            self.articlebydate = []


class Home(homeBase):
    def get(self):
        homeBase.init(self)
        self.title = 'Home'
		#lizhuang 改了
        industryList = ['multiple','consistency','advance','chemical','mechanical','computer','car','trade','medicine']
        if lang_encode == 'zh_CN':
            list1 = [item for item in self.categoryList[0].cateofa if item.abc == 0 ]
            list2 = [item for item in self.categoryList[1].cateofa if item.abc == 0 ]
            list3 = [item for item in self.categoryList[2].cateofa if item.abc == 0 ]
            list4 = [item for item in self.categoryList[3].cateofa if item.abc == 0 ]
            list5 = [item for item in self.categoryList[4].cateofa if item.abc == 0 ]

        else:
            list1 = [item for item in self.categoryList[0].cateofa if item.abc == 1 ]
            list2 = [item for item in self.categoryList[1].cateofa if item.abc == 1 ]
            list3 = [item for item in self.categoryList[2].cateofa if item.abc == 1 ]
            list4 = [item for item in self.categoryList[3].cateofa if item.abc == 1 ]
            list5 = [item for item in self.categoryList[4].cateofa if item.abc == 1 ]

        self.render('home_index.html', list1 = list1, list2 = list2, list3 = list3, list4 = list4, list5 = list5, industryList = industryList)
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
        if lang_encode == 'zh_CN':
            aList = self.session.query(Category).filter(Category.cid == cid).first().cateofa
            List = [item for item in aList if item.abc == 0]
        else:
            aList = self.session.query(Category).filter(Category.cid == cid).first().cateofa
            List = [item for item in aList if item.abc == 1]
        category = self.session.query(Category).filter(Category.cid == cid).first()
        self.title = category.cname
        targetpage = int(self.get_argument('page',default='1'))
        articleList, self.pagination = generatePagination('/c/'+cid+'?page=', List, targetpage)
        self.render('home_list.html', articleList = articleList, cid = cid)
        self.session.close()

class showAbout(homeBase):
    def get(self):
        homeBase.init(self)
        self.title = 'About Us'
        info_path = os.path.join(self.get_template_path(), 'aboutme.md')
        with open(info_path, 'r') as f:
            aboutcontent = f.read().decode('utf8')
        self.render('home_about.html', aboutcontent = aboutcontent)
        self.session.close()

class listByDate(staticBase):
    def get(self,cid,year,month):
        staticBase.init(self,cid)
        targetpage = int(self.get_argument('page',default='1'))
        articlelist = [article for article in self.session.query(Article).filter(Article.acid == cid).all() if article.acreatetime.year == int(year) and article.acreatetime.month == int(month)]
        articleList, self.pagination = generatePagination('/date/' + year + '/' + month + '/c/' + cid +'?page=', articlelist, targetpage)
        self.thisquery = "归档：" + str(year) + "年" + str(month) + "月"
        self.title = "归档：" + str(year) + "年" + str(month) + "月"
        self.render("home_list.html", articleList = articleList, cid = cid)
        self.session.close()
