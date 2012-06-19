# coding:utf-8

from _handler import Handler
from _urlmap import urlmap
from model.foo import getmsg
from model.foo import getreply
from model.foo import post_reply

@urlmap('/m/(\d+)')
class Msg(Handler):
    def get(self,id):
        r = getmsg(id)
        if not r:
            self.redirect('/')
        else:
            info = dict()
            info['id'] = r['id']
            info['who'] = r['who'].encode('utf-8')
            info['text'] = r['t'].encode('utf-8')
            if r['answer_id']:
                pass
            else:
                info['answer'] = '尚未产生'
        self.render(info=info,re=getreply(id))
    def post(self,id):
        who = self.get_argument('who','过客')
        t = self.get_argument('text','')
        post_reply(id,who,t)
        self.redirect('/m/%s'%id)

