# -*- coding:utf-8 -*-
import sys
import os.path

DEBUG = True 

PATH = os.path.abspath(os.path.dirname(__file__))

sys.path.append(os.path.join(PATH,".site-packages"))

from mako.lookup import TemplateLookup
MAKOLOOKUP = TemplateLookup(
    directories=os.path.join(PATH, 'htm'),
    #module_directory='/tmp/%s'%HTM_PATH.strip('/').replace('/', '.'),
    disable_unicode=True,
    encoding_errors='ignore',
    default_filters=['str', 'h'],
    filesystem_checks=DEBUG,
    input_encoding='utf-8',
    output_encoding=''
)


def render(htm, **kwds):
    mytemplate = MAKOLOOKUP.get_template(htm)
    return mytemplate.render(**kwds)


import tornado.database
try:
    import memcache
except ImportError:
    import pylibmc
#configs

import sae.const

if not sae.const.MYSQL_PASS:
    MYSQL_HOST = '127.0.0.1:3306'
    MYSQL_DB = 'sae'
    MYSQL_USER = 'sae'
    MYSQL_PWD = 'sae'
else:
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PWD = sae.const.MYSQL_PASS
    MYSQL_HOST = '%s:%s' % (sae.const.MYSQL_HOST, str(sae.const.MYSQL_PORT)) #sae.const.MYSQL_HOST_S ignore


_db = tornado.database.Connection(
    host=MYSQL_HOST, database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PWD, max_idle_time=5
)

try:
    _mc = memcache.Client(['127.0.0.1:11211'], debug=0)
except Exception:
    _mc = pylibmc.Client(['127.0.0.1:11211'])
