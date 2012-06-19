# coding:utf-8

def css(f):
    return '<link href="/static/css/%s"' % f + \
        ' rel="stylesheet" type="text/css">'

def js(f):
    return '<script src="/static/js/%s.js"></script>' %f

