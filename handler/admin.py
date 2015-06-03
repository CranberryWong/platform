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
        articleList = self.session.query(Article).all()
        self.render('admin_overview.html', articleList = articleList)
        self.session.close()

class EditPage(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        self.title = 'Dashboard Edit'
        aid = self.get_argument('aid', default=None)
        if aid == None:
            article = Article('','',1)
            article.aid = None
        else:
            article = self.session.query(Article).filter(Article.aid == aid).first()
        self.render('admin_editpage.html', active2 = 'class="active"', article = article)
        self.session.close()

    def post(self):
        self.title = 'Dashboard Edit'
        StaticData.init(self)
        aid = self.get_argument('aid', default='None')
        atitle = self.get_argument('atitle', default='')
        acontent = self.get_argument('acontent', default='')
        if pid == 'None':
            page = Page(ptitle, pcontent)
            if 'file' in self.request.files:
                file_dict_list = self.request.files['file']
                for file_dict in file_dict_list:
                    filename = nameRewrite(file_dict["filename"]).encode('utf8')
                    data = file_dict["body"]
                    image = Image.open(StringIO(data))
                    image.save(page_path + filename, quality=150)
                    '''
                    with open(page_path + filename, 'w') as f:
                        f.write(data)
                        print filename'''
                    page.ppic = '/static/page/' + filename
            self.session.add(page)
            self.session.commit()
        else:
            page = self.session.query(Page).filter(Page.pid == pid).first()
            page.ptitle = ptitle
            page.pcontent = pcontent
            if 'file' in self.request.files:
                file_dict_list = self.request.files['file']
                for file_dict in file_dict_list:
                    filename = nameRewrite(file_dict["filename"]).encode('utf8')
                    if page.ppic[:len(filename)-10] != '/static/page/' + filename[:len(filename)-10]:
                        print page.ppic[:len(filename)-10],'/static/page/' + filename[:len(filename)-10]
                        data = file_dict["body"]
                        image = Image.open(StringIO(data))
                        image.save(avatar_path + filename, quality=150)
                        page.ppic = '/static/page/' + filename
            page.pchgtime = datetime.now()
            self.session.commit()
        self.write('<script language="javascript">alert("提交成功");self.location="/admin/editpage"</script>')
        self.session.close()

class DelPage(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        pid = self.get_argument('pid', default=None)
        self.session.query(Page).filter(Page.pid == pid).delete()
        self.session.commit()
        self.redirect('/admin')
        self.session.close()

class TypeOption(StaticData):
    @tornado.web.authenticated
    def get(self):
        StaticData.init(self)
        self.title = 'Edit Category'
        categoryList = self.session.query(Category).all()
        cid = self.get_argument('cid', default=None)
        if cid == None:
            cateobj = Category('',1)
            cateobj.cid = None
        else:
            cateobj = self.session.query(Category).filter(Category.cid == cid).first()
        self.render('admin_type.html', categoryList = categoryList)
        self.session.close()

    def post(self):
        StaticData.init(self)
        cid = self.get_argument('cid', default='None')
        cname = self.get_argument('cname', default='')
        if cid == 'None':
            cateobj = Category(typename)
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
        pass

    def post(self):
        pass

class DelLink(StaticData):
    def get(self):
        pass
