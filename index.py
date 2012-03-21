#encoding=utf-8
#author:fly123
#date:2012/2/28

from config import *
import sys
import sqlite3
import function



app = web.application(urls, globals())



#db =  sqlite3.connect('web_terminal.db')
#store = web.session.DBStore(db, 'sessions')
#
#
#
#if web.config.get('_session') is None:   
#    session = web.session.Session(app, store,initializer=session_values)   
#    web.config._session = session
#else:
#    session = web.config._session   
#    
#    
#def session_hook():
#    web.ctx.session = session
#    web.template.Template.globals['session'] = session




class index:
    def GET(self):
        #if function.IsLogged():
        global isLogin
        if 1: #isLogin == 1:
            #return render.index('system is ' + current_system) 
            return render.gui_index('')
        return render.login(0)
    
class Login:
    def POST(self):
        i = web.input()
        user_name = i.username
        password = i.password
        logging.info(u"登录验证：<username='%s', password='%s'>" % (user_name, password))
        if (user_name == 'fly123' and password == 'scut'):
            #function.Login(user_name, 1) 
            global isLogin
            isLogin = 1   
            return 1

        #登录失败 
        logging.info(u"登录失败: <username='%s', password='%s'>" % (user_name, password))
        return 0
            
# /logout
# 登出页面
# 
class Logout:
    def GET(self):
        function.Logout()
        raise web.seeother('/')
    
#def initialize():
#    sys.path.append('/home/fly123/workspace/web_terminal/') 

if __name__ == "__main__":
#    app.add_processor(web.loadhook(session_hook))
    app.run()
