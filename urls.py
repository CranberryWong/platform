#! /usr/bin/env python
#coding=utf-8

from handler import home, admin, upload

homeurls = [

   #前台
   (r"/",home.Home),
   (r"/c/([0-9]+)/a/([0-9]+)",home.showArticle),
   (r"/c/([0-9]+)",home.showList),
   (r"/aboutus",home.showAbout),
   (r"/signin",admin.Signin),
   (r"/signout",admin.Signout),
   (r"/admin",admin.AdminHome),
   (r"/admin/changearticlechecked",admin.ChangeArticleChecked),
   (r"/admin/editpage",admin.EditPage),
   (r"/admin/delpage",admin.DelPage),
   (r"/admin/edittype",admin.TypeOption),
   (r"/admin/deltype",admin.DelType),
   (r"/admin/changetypechecked",admin.ChangeTypeChecked),
   (r"/admin/editlink",admin.LinkOption),
   (r"/admin/dellink",admin.DelLink),
   (r"/upload?",upload.ImageUpload),
   (r'/c/([0-9]+)/date/([0-9]+)/([0-9]+)',home.listByDate),
]
