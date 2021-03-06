#encoding=utf-8
#author:fly123
#date:2012/2/28

import subprocess
import time
from  model import utility
from config import render 

class LinuxGUI:
    def __init__(self):
        self.input = 'model/stdio/input' 
        self.output = 'model/stdio/output' 
        self.error = 'model/stdio/error' 
        
        output = open(self.output, 'w+')

        self.subprocess = subprocess.Popen(['bash'], stdin = subprocess.PIPE, 
                stdout = output, stderr = output, shell = False) 

        #这个也是具体而定
        self.user = 'fly123' 
        self.ttynum = 1         
        self.start_time = 0

    def receiveorder(self, order):
        if order == 'clear':
            utility.clearoutput(self.output)
            return render.index('') 
        order = order + '\n'
        self.subprocess.stdin.write('echo "-->"' + order + ' pwd\n')
        time.sleep(0.1)
        self.subprocess.stdin.write(order) 


    def response(self):
        output = open(self.output)
        string = ''
        for line in output.readlines():
            string += line + "<br/>"
        output.close()
        return string

