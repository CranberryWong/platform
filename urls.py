#! /usr/bin/env python
#coding=utf-8

from handler import home, admin, upload

homeurls = [

   #前台
   (r"/",home.Home),
   (r"/signin",admin.Signin),
   (r"/admin",admin.AdminHome),
   (r"/admin/editpage",admin.EditPage),
   (r"/admin/delpage",admin.DelPage),
   (r"/admin/edittype",admin.TypeOption),
   (r"/admin/deltype",admin.DelType),
   (r"/upload?",upload.ImageUpload),
]
