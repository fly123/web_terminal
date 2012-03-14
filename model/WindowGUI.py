#encoding=utf-8
#author:fly123
#date:2012/3/6

import subprocess
import time
from  model import utility
from config import * 
import shutil
import os
import _winreg

class WindowGUI:
    def __init__(self):
        self.input = 'model/stdio/input' 
        self.output = 'model/stdio/output' 
        self.error = 'model/stdio/error' 
        self.order = ''
        self.desktop = self.get_desktop()
        #Ϊ��upload
        self.web_input = ''

        self.output_fd = open(self.output, 'w+')

    def receiveorder(self, web_input):
        return 0
#        self.web_input = web_input
#        self.order = web_input.order 
#        if self.order == 'cls':
#            utility.clearoutput(self.output)
#            return render.index('')
#        if self.order.split(' ')[0] == 'download' or self.order.split(' ')[0] == 'upload':
#            return ''
#        self.subprocess.stdin.write(self.order + '\n') 

    def response(self):
#        if self.order.split(' ')[0] == 'download':
#            oprand = self.order.split(' ')[1]
#            src_dir = self.get_current_dir()  + ''.join(self.order.split(' ')[1])
#            des_dir = 'static\\tmp\\' + ''.join(oprand.split('\\')[-1:])
#            shutil.copyfile(src_dir, des_dir)
#            return des_dir.replace('\\', '/')
#
#
#        elif self.order.split(' ')[0] == 'upload': 
#            x = self.web_input
#            #x = self.web_input(fileUpload={})
#            if 'fileUpload' in x: # to check if the file-object is created
#                filedir = self.order.split(' ')[1] 
#                filepath=x.fileUpload.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
#                filename =filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
#                #fout = open(filedir + '/' + filename,'w') # creates the file where the uploaded file should be stored
#                fout = open(filedir + '\\' + filename, 'w')
#                fout.write(x.fileUpload.file.read()) # writes the uploaded file to the newly created file.
#                fout.close() # closes the file, upload complete.   
#
#
        self.traversal(self.desktop)
        self.get_icon(self.desktop)
        self.output_fd.close()
        output = open(self.output)
        string = ''
        for line in output.readlines():
            string += line + "<br/>"
        output.close()
        return string
    
    def traversal(self, direction):
        lst = os.listdir(direction)
        for it in lst:
            it = direction + '\\' + it 
            isFile = os.path.isfile(it)
            if isFile:
                self.output_fd.write('\t' + it + '\tfile\n')
                
            else:
                self.output_fd.write('\t' + it + '\tfolders\n') 
                #self.traversal(it)

    def get_disk_partition(self):
        for it in range(ord('a'), ord('z') + 1):
            it = chr(it) + ':\\'
            if os.path.isdir(it):
                print it
                self.traversal(it)
                
    def get_desktop(self):
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,\
                              r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
        return _winreg.QueryValueEx(key, "Desktop")[0] 
    
    def get_icon(self, path):
        

    
        
