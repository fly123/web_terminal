#encoding=utf-8
#author:fly123
#date:2012/2/25


import web
from config import *

def IsLogged():
    return web.ctx.session.IsLogin == 1

def Login(username, userid):
    logging.info(u"登录: <username='%s', userid='%s'>" % (username, userid))
    web.ctx.session.IsLogin = 1
    web.ctx.session.username = username
    web.ctx.session.userID = userid
    
def Logout():
    logging.info(u"注销: <username='%s', userid='%s'>" % (web.ctx.session.username, web.ctx.session.userID))
    web.ctx.session.IsLogin = 0
    web.ctx.session.kill()
    
def GetSessionUserID():
    return web.ctx.session.userID

# 获取当前会话用户名
def GetSessionUserName():
    return web.ctx.session.username



