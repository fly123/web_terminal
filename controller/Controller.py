#encoding=utf-8
#author:fly123
#date:2012/2/27


from model.LinuxShell import *
from model.WindowShell import *
from model.WindowGUI import *
from config import *
import web

a = 'nothing'

class Controller:

    connect_num = 0


    def POST(self):
        web_input = web.input(fileUpload={})
        return self.maintain_connect(web_input)

    def __init__(self):
        self.func_map = { '1' : self.end_connect }
        self.connect_list = ['first'] 
        
    
    def build_connect(self):
        self.connect_list.append('12')
        self.connect_num += 1

    def maintain_connect(self, web_input):
        global a, isLogin 
        if (a == 'nothing'):
            if current_system == 'Linux':
                a = LinuxShell()
            elif current_system == 'Windows':
                a = WindowShell()
            
            
            #a = WindowGUI()
        a.receiveorder(web_input)
        time.sleep(0.2)
        return  a.response()

    def end_connect(self):
        Controller.connect_num -= 1
        print '%' * 50
        print 'connect end...'
