#encoding=utf-8
#author:fly123
#date:2012/2/27

from config import *
import web

if current_system == 'Windows':
    from model.WindowShell import *
    from model.WindowGUI import *
else:
    from model.LinuxShell import *


a = 'nothing'
MODE = 'Normal'
#IPADDR = '127.0.0.1:'

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
        global a, isLogin, MODE 
        if (a == 'nothing'):
            if current_system == 'Linux':
                a = LinuxShell()
            elif current_system == 'Windows':
                a = WindowShell()
                
        if web_input.order == 'AllInOne':
            MODE = 'AllInOne'
            return  'AllInOne'
        #MODE = 'AllInOne'    
        if MODE == 'AllInOne':
            self.synchronously(web_input) 
            #a = WindowGUI()
        a.receiveorder(web_input)
        time.sleep(0.2)
        return  a.response()

    def end_connect(self):
        Controller.connect_num -= 1
        print '%' * 50
        print 'connect end...'
        
        
#synchronously
    def synchronously(self, web_input):
#        print web_input
#        print web_input.fileUpload
#        fields = [
#                  (u'order', str(web_input.order)),
#                  (u'fileUpload', web_input.fileUpload)
#                  ]
#    
#        pc = pycurl.Curl()
#        pc.setopt(pycurl.POST, 1) # POST method
#        pc.setopt(pycurl.URL, 'http://127.0.0.1:1234/receiveorder') # 上传的API接口
#        pc.setopt(pc.HTTPPOST, fields)
#        
#        pc.perform() # Actually do POST request, 文件上传
#        pc.close()
        import urllib, urllib2
        #data = urllib.urlencode({'order': web_input.order, 'fileUpload' : (web_input.fileUpload.filename, web_input.fileUpload.file.read())}) 
        data = urllib.urlencode({'order' : web_input.order, 'fileUpload' : web_input.fileUpload})
        request = urllib2.Request('http://127.0.0.1:1234/receiveorder', data) 
        response = urllib2.urlopen(request)
        file = response.read()
        print file
        
        
        
