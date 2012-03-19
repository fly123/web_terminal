#encoding=utf-8
#author:fly123
#date:2012/2/28

import subprocess
import time
from  model import utility
from config import * 
import shutil
import codecs

class WindowShell:
    def __init__(self):
        self.input = 'model/stdio/input' 
        self.output = 'model/stdio/output' 
        self.error = 'model/stdio/error' 
        self.order = ''
        #为了upload
        self.web_input = ''

        output = open(self.output, 'w+')

        self.subprocess = subprocess.Popen(['cmd'], stdin = subprocess.PIPE, 
                stdout = output, stderr = output, shell = False) 

        self.user = 'fly123' 
        self.ttynum = 1         
        self.start_time = 0

    def receiveorder(self, web_input):
        self.web_input = web_input
        self.order = web_input.order 
        if self.order == 'cls':
            utility.clearoutput(self.output)
            return render.index('')
        if self.order.split(' ')[0] == 'download' or self.order.split(' ')[0] == 'upload':
            #暂时不让download ，upload回显
            #self.subprocess.stdin.write('echo "-->"' + order + ' echo%cd%\n') 
            return ''
        self.subprocess.stdin.write(self.order + '\n') 

    def response(self):
        if self.order.split(' ')[0] == 'download':
            oprand = self.order.split(' ')[1]
            src_dir = self.get_current_dir()  + ''.join(self.order.split(' ')[1])
            des_dir = 'static\\tmp\\' + ''.join(oprand.split('\\')[-1:])
            shutil.copyfile(src_dir, des_dir)
            #这里需要把\\变为/，因为http的路径方·式
            return des_dir.replace('\\', '/')


        elif self.order.split(' ')[0] == 'upload': 
            x = self.web_input
            
            if 'fileUpload' in x: # to check if the file-object is created
                filedir = self.order.split(' ')[1] 
                filename = ''
                content = ''
                if (type(x.fileUpload) == type('str')):
                    tmpstr = x.fileUpload
                    first = tmpstr.find('(')
                    mytuple = eval(tmpstr[first:])
                    
                    filename = mytuple[1]
                    content = mytuple[2]
                    
                else:
                    filepath=x.fileUpload.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
                    filename =filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
                    content = x.fileUpload.file.read()
                    
                fout = open(filedir + '\\' + filename, 'w')
                fout.write(content) # writes the uploaded file to the newly created file.
                fout.close() # closes the file, upload complete.   


        output = codecs.open(self.output, 'r', 'gbk')
        string = ''
        for line in output.readlines():
            string += line + "<br/>"
        string = string.replace(u'<DIR>', u'DIR')
        output.close()
        return string
    
    def get_current_dir(self):
        output = open(self.output)
        last_line = output.readlines()[-1:]
        output.close()
        #消掉最后的>变为\
        return (''.join(last_line) )[:-1] + '\\'

    
        
