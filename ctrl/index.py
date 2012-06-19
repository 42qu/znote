#coding:utf-8

from _handler import Handler
from _urlmap import urlmap
from model.foo import getmsgs
from model.foo import post_msg

@urlmap('/')
class Index(Handler):
    def get(self):
        msg_lst = []
        ret = getmsgs()
        if ret:
            for i in ret:
                m = dict()
                m['id'] = i['id']
                m['who'] = i['who']
                m['text'] = i['t'].encode('utf-8')
                if i['answer_id']:
                    pass
                else:
                    m['answer'] = '尚未产生'
                msg_lst.append(m)
        self.render(msg_lst=msg_lst)
    def post(self):
        who = self.get_argument('who','过客')
        t = self.get_argument('text','')
        post_msg(who,t)
        self.redirect('/')

