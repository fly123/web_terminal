#encoding=utf-8
#author:fly123
#date:2012/2/27

import web

render = web.template.render('templates/')


urls = (
        '/', 'index',
        '/receiveorder', 'controller.Controller.Controller'
        )
