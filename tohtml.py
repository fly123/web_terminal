#encoding=utf-8
#author:luojiafei
#data:2012/2/15

import re
def txtTohtml():
    output = open('stdio/output')
    list_of_lines = output.readlines()
    string = ''
    for line in list_of_lines:
        string += line + "<br/>"
    output.close() 
    return string
