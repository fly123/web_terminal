#encoding=utf-8
#author:fly123
#date:2012/2/27

import web
import platform

render = web.template.render('templates/')
current_system = platform.system()

urls = (
        '/', 'index',
        '/receiveorder', 'controller.Controller.Controller'
        )

#暂时先这样记下upload的路径
UPLOAD_DIR = ' '
