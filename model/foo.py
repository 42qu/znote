#!/usr/bin/env python

from _db import _db

def post_msg(who,text):
    return _db.execute('insert into `msg` (who,t) values (%s,%s)',
            who,text)

def post_reply(msg_id,who,text):
    return _db.execute(
        'insert into `reply` (msg_id,who,t) values (%s,%s,%s)',
        msg_id,who,text)

def chooseanswer(msg_id,reply_id):
    pass

def getmsgs(limit=10):
    return _db.query('select * from `msg` limit %s' % limit);

def getmsg(id):
    return _db.get('select * from `msg` where id=%s' % id);

def getreply(msg_id):
    return _db.query('select * from `reply` where msg_id=%s' % msg_id);

def search(text):
    pass
    #select * from `msg` like ``

if __name__ == "__main__":
    pass
    #'''create table msg(id integer primary key auto_increment,
    #        who text, t text,answer_id integer)'''

    #'''create table reply(id integer primary key auto_increment,
    #        msg_id integer, who text, t text)'''

