# -*- coding: utf-8 -*-
# filename: main.py
import web
import hashlib


class Handle(object):
    def GET(self):
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "YaoJiexian02" #此处我填了自己的，需要将其替换成你们自己公众平台官网\基本配置中的Token

            list = [token,timestamp,nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(list[0].encode("utf-8"))
            sha1.update(list[1].encode("utf-8"))
            sha1.update(list[2].encode("utf-8"))
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr

        
urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
