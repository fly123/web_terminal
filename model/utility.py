#encoding=utf-8
#author:fly123
#date:2012/2/28

def clearoutput(output_name):
    output = open('model/stdio/output', 'r+')
    output.truncate()
    output.close()
