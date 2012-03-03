#encoding=utf-8
#author:fly123
#date:2012/2/28

import subprocess
import time
from  model import utility
from config import * 
import shutil

class WindowShell:
    def __init__(self):
        self.input = 'model/stdio/input' 
        self.output = 'model/stdio/output' 
        self.error = 'model/stdio/error' 
        self.order = ''

        output = open(self.output, 'w+')

        self.subprocess = subprocess.Popen(['cmd'], stdin = subprocess.PIPE, 
                stdout = output, stderr = output, shell = False) 

        self.user = 'fly123' 
        self.ttynum = 1         
        self.start_time = 0

    def receiveorder(self, order):

        self.order = order
        if order == 'cls':
            utility.clearoutput(self.output)
            return render.index('')
        order = order + '\n'
        if order.split(' ')[0] == 'download':
            return ''
        self.subprocess.stdin.write(order) 

    def response(self):
        if self.order.split(' ')[0] == 'download':
            oprand = self.order.split(' ')[1]
            src_dir = self.get_current_dir()  + ''.join(self.order.split(' ')[1])
            des_dir = 'static\\tmp\\' + ''.join(oprand.split('\\')[-1:])
            shutil.copyfile(src_dir, des_dir)
            #这里需要把\\变为/，因为http的路径方·式
            return des_dir.replace('\\', '/')
        output = open(self.output)
        string = ''
        for line in output.readlines():
            string += line + "<br/>"
        output.close()
        return string
    
    def get_current_dir(self):
        output = open(self.output)
        last_line = output.readlines()[-1:]
        output.close()
        #消掉最后的>变为\
        return (''.join(last_line) )[:-1] + '\\'

    
        
