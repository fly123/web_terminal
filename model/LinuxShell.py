#encoding=utf-8
#author:fly123
#date:2012/2/28

import subprocess
import time
from  model import utility
from config import * 
import shutil

class LinuxShell:
    def __init__(self):
        self.input = 'model/stdio/input' 
        self.output = 'model/stdio/output' 
        self.error = 'model/stdio/error' 
        self.order = ''
        self.web_input = ''
        
        output = open(self.output, 'w+')

        self.subprocess = subprocess.Popen(['bash'], stdin = subprocess.PIPE, 
                stdout = output, stderr = output, shell = False) 

        #这个也是具体而定
        self.user = 'fly123' 
        self.ttynum = 1         
        self.start_time = 0

    def receiveorder(self, web_input):
        
        self.web_input = web_input
        self.order = web_input.order
        if self.order == 'clear':
            utility.clearoutput(self.output)
            return render.index('') 
        self.subprocess.stdin.write('echo "-->"' + self.order  + '\n' + ' pwd\n')
        time.sleep(0.1)
        if self.order.split(' ')[0] == 'download' or self.order.split(' ')[0] == 'upload':
            return ''
        self.subprocess.stdin.write(self.order + '\n') 

    def response(self):
        if self.order.split(' ')[0] == 'download':
            oprand = self.order.split(' ')[1]
            src_dir=self.get_current_dir()[:-1] + '/' + ''.join(self.order.split(' ')[1]) 
            des_dir = 'static/tmp/' + ''.join(oprand.split('/')[-1:])
            shutil.copyfile(src_dir, des_dir)
            return des_dir 
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
                    
                fout = open(filedir + '/' + filename, 'w')
                fout.write(content) # writes the uploaded file to the newly created file.
                fout.close() # closes the file, upload complete.           
                
                
        output = open(self.output)
        string = ''
        for line in output.readlines():
            string += line + "<br/>"
        output.close()
        return string
 
#这里不知道output用pipe为什么不行
#好像不能在一个进程用两个stdin都为pipe, 而至少一个stdout为pipe的
    def get_current_dir(self):
        #pwd = open('model/stdio/pwd', 'w')
        #tmp_process = subprocess.Popen(['bash'], stdin = subprocess.PIPE, 
        #        stdout = pwd, stderr = pwd, shell = False) 
        #tmp_process.stdin.write('pwd\n')
        #pwd.close() 
        #current_dir = ''
        #time.sleep(0.1)
        #pwd = open('model/stdio/pwd') 
        #for line in pwd.readlines():
        #    current_dir += line
        #pwd.close()
        #tmp_process.kill()
        #print '77' * 90
        #print current_dir 
        #return current_dir

#current_dir is the last line
        output = open(self.output)
        last_line = output.readlines()[-1:]
        output .close()
        return ''.join(last_line)





