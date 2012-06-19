import tornado.web
from config import render

def lower_name(class_name):
    """
    >>>lower_name("UserCount")
    'user_count'

    >>>lower_name("user_count")
    'user_count'
    """
    result = []
    for c in class_name:
        i = ord(c)
        if 65 <= i <= 90:
            if result:
                if not 48 <= ord(result[-1]) <= 57:
                    result.append('_')
            i += 32
            c = chr(i)
        result.append(c)
    return ''.join(result)


class Handler(tornado.web.RequestHandler):
    def render(self, template_name=None, **kwds):
        if template_name is None:
            if not hasattr(self, 'template'):
                self.template = '%s/%s.htm' % (
                    self.__module__[5:].replace('.', '/'),
                    lower_name(self.__class__.__name__)
                )
            template_name = self.template

        current_user = self.current_user
        kwds['current_user'] = current_user
        kwds['request'] = self.request
        kwds['this'] = self
        #kwds.update(RENDER_KWDS)
        if not self._finished:
            self.finish(render(template_name, **kwds))

