import sys
import os.path
PATH = os.path.abspath(os.path.dirname(
    os.path.dirname(__file__)
))
sys.path.append(PATH)

from config import MYSQL_HOST, MYSQL_PWD, MYSQL_USER, MYSQL_PWD, MYSQL_DB 

import tornado.database

_db =  tornado.database.Connection(
    host=MYSQL_HOST,database=MYSQL_DB,user=MYSQL_USER,password=MYSQL_PWD, max_idle_time = 5
)
