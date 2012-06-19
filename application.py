import tornado.wsgi
import os.path
import sys
from config import DEBUG
from ctrl import _urlmap, _url

settings = {
    'debug':DEBUG,
}

application = tornado.wsgi.WSGIApplication(
    tuple(_urlmap.urlmap.handlers)
    , 
    **settings
)




