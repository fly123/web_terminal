#encoding=utf-8
#author:fly123
#date:2012/2/27


from model.LinuxShell import *
from model.WindowShell import *
from config import *
import web

a = 'nothing'

class Controller:

    connect_num = 0
    isLogin = 0


    def POST(self):
        i = web.input()
        return self.maintain_connect(i.order)

    def __init__(self):
        self.func_map = { '1' : self.end_connect }
        self.connect_list = ['first'] 
        
        Controller.isLogin += 1
    
    def build_connect(self):
        self.connect_list.append('12')
        connect_num += 1

    def maintain_connect(self, order):
        global a
        if (Controller.isLogin == 1):
            if current_system == 'Linux':
                a = LinuxShell()
            elif current_system == 'Windows':
                a = WindowShell()
        a.receiveorder(order)
        time.sleep(0.1)
        return  a.response()

    def end_connect(self):
        Controller.connect_num -= 1
        print '%' * 50
        print 'connect end...'
