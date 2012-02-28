#encoding=utf-8
#author:fly123
#date:2012/2/28

from config import *
import platform
import sys


app = web.application(urls, globals())


class index:
    def GET(self):
      return render.index('system is ' +platform.system()) 

#def initialize():
#    sys.path.append('/home/fly123/workspace/web_terminal/') 

if __name__ == "__main__":
    app.run()
