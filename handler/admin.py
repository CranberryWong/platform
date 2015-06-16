#! /usr/bin/env python
#coding:utf-8

import tornado.web
import time
import os
import markdown
from models.entity import Article, Category, Link, Setting
from models.entity import db_session
import hashlib
import json
import random
from datetime import datetime
from PIL import Image

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

class SignValidateBase(tornado.web.RequestHandler):
   def get_current_user(self):
      return self.get_secure_cookie('username')

class StaticData(SignValidateBase):
   def init(self):
      self.session = db_session.getSession

class Signin(SignValidateBase):
   def get(self):
      self.title = 'Sign in'
      self.render('signin.html')

   def post(self):
      self.session = db_session.getSession
      username = self.get_argument('username', default='')
      password = self.get_argument('password', default='')
      md5_psw = hashlib.md5(password).hexdigest()
      user = self.session.query(Setting).filter(Setting.sadmin==username).one()
      uname = user.sadmin
      psw = user.spwd
      if username == uname and md5_psw == psw:
         self.set_secure_cookie('username', username)
         self.redirect('/admin')
      else:
         self.write('<script language="javascript">alert("用户名或密码错误");self.location="/signin";</script>')
      self.session.close()

class Signout(SignValidateBase):
   def get(self):
      self.clear_cookie('username')
      self.redirect('/')
'''
class ChangePwd(SignValidateBase):
    def get(self):
        #self.render('')

    def post(self):
        #newpwd = self.get_argument('password', default='')
        self.session = db_session.getSession
        pass
'''

class AdminHome(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        self.title = 'Dashboard'
        List = self.session.query(Article).all()
        targetpage = int(self.get_argument('page',default='1'))
        articleList, self.pagination = generatePagination('/admin?page=', List, targetpage)
        self.render('admin_overview.html', articleList = articleList)
        self.session.close()

class EditPage(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        self.title = 'Edit Article'
        aid = self.get_argument('aid', default=None)
        if aid == None:
            article = Article('','',1)
            article.aid = None
        else:
            article = self.session.query(Article).filter(Article.aid == aid).first()
        categoryList = self.session.query(Category).all()
        self.render('admin_editpage.html', active2 = 'class="active"', article = article, categoryList = categoryList)
        self.session.close()

    def post(self):
        self.title = 'Dashboard Edit'
        StaticData.init(self)
        aid = self.get_argument('aid', default='None')
        atitle = self.get_argument('atitle', default='')
        acontent = self.get_argument('acontent', default='')
        acategory = self.get_argument('acategory', default='')
        acid = self.session.query(Category).filter(Category.cname == acategory).first().cid
        if aid == 'None':
            article = Article(atitle, acontent, acid)
            self.session.add(article)
            self.session.commit()
        else:
            article = self.session.query(Article).filter(Article.aid == aid).first()
            article.atitle = atitle
            article.acontent = acontent
            article.acid = acid
            article.amodifytime = datetime.now()
            self.session.commit()
        self.write('<script language="javascript">alert("提交成功");self.location="/admin"</script>')
        self.session.close()

class DelPage(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        aid = self.get_argument('aid', default=None)
        self.session.query(Article).filter(Article.aid == aid).delete()
        self.session.commit()
        self.redirect('/admin')
        self.session.close()

class ChangeArticleChecked(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        aid = self.get_argument('aid')
        achecked = self.get_argument('acheck')
        print aid, achecked, type(achecked)
        if achecked == 'False':
            achecked = False
        else:
            achecked = True
        article = self.session.query(Article).filter(Article.aid == aid).first()
        article.acheck = not achecked
        self.session.commit()
        self.redirect('/admin')
        self.session.close()

class ChangeTypeChecked(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        cid = self.get_argument('cid')
        cchecked = self.get_argument('ccheck')
        if cchecked == 'False':
            cchecked = False
        else:
            cchecked = True
        category = self.session.query(Category).filter(Category.cid == cid).first()
        category.ccheck = not cchecked
        self.session.commit()
        self.redirect('/admin/edittype')
        self.session.close()

class TypeOption(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        self.title = 'Edit Category'
        categoryList = self.session.query(Category).all()
        cid = self.get_argument('cid', default=None)
        if cid == None:
            cateobj = Category('')
            cateobj.cid = None
        else:
            cateobj = self.session.query(Category).filter(Category.cid == cid).first()
        self.render('admin_type.html', categoryList = categoryList, cateobj = cateobj)
        self.session.close()

    def post(self):
        StaticData.init(self)
        cid = self.get_argument('cid', default='None')
        cname = self.get_argument('cname', default='')
        if cid == 'None':
            cateobj = Category(cname)
            self.session.add(cateobj)
            self.session.commit()
        else:
            cateobj = self.session.query(Category).filter(Category.cid == cid).first()
            cateobj.cname = cname
            self.session.commit()
        self.redirect('/admin/edittype')
        self.session.close()

class DelType(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        cid = self.get_argument('cid', default=None)
        self.session.query(Category).filter(Category.cid == cid).delete()
        self.session.commit()
        self.redirect('/admin/edittype')
        self.session.close()

class LinkOption(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        self.title = 'Edit Link'
        linkList = self.session.query(Link).all()
        lid = self.get_argument('lid', default=None)
        if lid == None:
            linkobj = Link('', '')
            linkobj.lid = None
        else:
            linkobj = self.session.query(Link).filter(Link.lid == lid).first()
        self.render('admin_link.html', linkList = linkList, linkobj = linkobj)
        self.session.close()

    def post(self):
        StaticData.init(self)
        lid = self.get_argument('lid', default='None')
        ltitle = self.get_argument('ltitle', default='')
        lurl = self.get_argument('lurl', default='')
        if lid == 'None':
            linkobj = Link(ltitle, lurl)
            self.session.add(linkobj)
            self.session.commit()
        else:
            linkobj = self.session.query(Link).filter(Link.lid == lid).first()
            linkobj.ltitle = ltitle
            self.session.commit()
        self.redirect('/admin/editlink')
        self.session.close()

class DelLink(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        cid = self.get_argument('lid', default=None)
        self.session.query(Link).filter(Link.lid == lid).delete()
        self.session.commit()
        self.redirect('/admin/editlink')
        self.session.close()

class SettingsOption(StaticData):
    @tornado.web.authenticated
    def get(self):
        self.title = 'Edit About'
        StaticData.init(self)
        info_path = os.path.join(self.get_template_path(), 'aboutme.md')
        with open('info_path', 'r') as f:
            aboutcontent = f.read().decode('utf8')
        self.render('admin_aboutus.html', aboutcontent = aboutcontent)
        self.session.close()

    def post(self):
        info_path = os.path.join(self.get_template_path(), 'aboutme.md')
        aboutcontent = self.get_argument('siteabout', default='')
        with open('info_path', 'w') as f:
            f.write(aboutcontent.encode('utf8'))
        self.write('<script language="javascript">alert("提交成功");self.location="/admin/aboutus";</script>')
