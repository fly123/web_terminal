#encoding=utf-8
#author:luojiafei
#data:2012/2/12
#title:main logic

import web
import subprocess
import time
import sys
import tohtml

p = 'nothing' 


urls = (
  '/', 'index',
  '/receiveorder', 'receiveorder',
  '/clearall', 'clearall'
)

render = web.template.render('templates/')

app = web.application(urls, globals())

isLogin = 0
class index:
    def GET(self):
        if isLogin:
            pass
        else:
            login()
        return render.index('ok')

class receiveorder:
    def GET(self):
        i = web.input()
        order = i.order + '\n'
        readshell(order)
        time.sleep(0.1)
        content = response() 
        return render.index(content)
        
    def POST(self):
        i = web.input()
        if i.order == 'clear':
            clearoutput()
            return 'ok'
        order = i.order + '\n'
        readshell(order)
        time.sleep(0.1)
        content = tohtml.txtTohtml()
        return content 


def readshell(order):
    global p
    p.stdin.write('echo order:' + order + ' pwd\n')
    time.sleep(0.2)
    p.stdin.write(order)
        

def response():
        output = open('stdio/output')
        list_of_lines = output.readlines()
        string = ''
        for line in list_of_lines:
            string += line;
        return string

class clearall:
    def GET(self):
        clearoutput()
        return render.index('ok')


def clearoutput():
        output = open('stdio/output', 'r+');
        output.truncate()
        output.close()
#def makesubprocess():
#        order = 'who'
#        p = subprocess.Popen(order, stdin = subprocess.PIPE, 
#                stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
#        
#        return render.index(p.stdout.read())

def test_login():
    subapp = 'su' 
    #order = ' 127.0.0.1 -l root'
    order = '-l'
    file = '1.txt'
    args = [subapp]

   # input = open('/dev/pts/0', 'w+')
    input = open('/dev/stdin', 'w+')
    output = open('output', 'w+')
    error = open('error','w+')
    
    #subprocess.PIPE = input
   # p = subprocess.Popen(['su'], stdin = subprocess.PIPE, 
   #          stdout = output, stderr = error, shell = False)
    p = subprocess.Popen(['ssh','root@127.0.0.1'], stdin = input, 
             stdout = output, stderr = error, shell = False)
    p.stdin = input
    #time.sleep(20)
    p.stdin.write('ls\n')
    login_input = open('/dev/pts/4', 'w+')
    login_input.write('ls\n')
    #p.stdin.write('help\n')
    #p.stdin.write('l\n')
    #p.stdin.write('quit\n')

    #print p.stdout.read()
    #input.write('help\n\n')
    #time.sleep(100)
    p.wait()
    #p.stdin.write('help\n')


   #p.stdin.write('3\r')
    #p.stdin.write('4\r')
    #print p.stdout.read()
    #time.sleep(2)



def login():
    global p, isLogin

    input = open('stdio/input', 'w+')
    output = open('stdio/output', 'w+')
    error = open('stdio/error', 'w+') 

#    p = subprocess.Popen(['ssh', 'root@127.0.0.1'], stdin = subprocess.PIPE, 
#             stdout = output, stderr = output, shell = False)
    p = subprocess.Popen(['bash'], stdin = subprocess.PIPE, 
             stdout = output, stderr = output, shell = False)
    #p.stdin.write('pwd\n')
    #p.stdin.write('cd /home/fly123\n')
    #p.stdin.write('pwd\n')
    #p.stdin.write('ls\n')
    #p.stdin.write('logout\n')
    #p.wait()
    isLogin = 1
    print 'subprocess finish\n'
        
if __name__ == "__main__": 
    app.run()

