#encoding=utf-8
#author:fly123
#date:2012/2/28

import subprocess
import time
from  model import utility
from config import render 

class WindowShell:
    def __init__(self):
        self.input = 'model/stdio/input' 
        self.output = 'model/stdio/output' 
        self.error = 'model/stdio/error' 
        self.special_order = ['download', 'upload']

        output = open(self.output, 'w+')

        self.subprocess = subprocess.Popen(['cmd'], stdin = subprocess.PIPE, 
                stdout = output, stderr = output, shell = False) 

        self.user = 'fly123' 
        self.ttynum = 1         
        self.start_time = 0

    def receiveorder(self, order):
        if order == 'cls':
            utility.clearoutput(self.output)
            return render.index('')
        if order == 'download':
            self.special_response(order)
        order = order + '\n'
        #self.subprocess.stdin.write('echo "-->"' + order + ' echo %cd%\n')
        time.sleep(0.1)
        self.subprocess.stdin.write(order) 

    def response(self):
        output = open(self.output)
        string = ''
        for line in output.readlines():
            string += line + "<br/>"
        output.close()
        return string
    
    def special_response(self, order):
        tmp_process = subprocess.Popen(['cmd'], stdin = subprocess.PIPE, 
                stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False) 
        tmp_process.stdin.write('echo %cd%\n')
        print tmp_process.stdout.read()
        print '*' * 90
