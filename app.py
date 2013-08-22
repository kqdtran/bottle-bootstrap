#!/usr/bin/env python

import os
from bottle import route, run, static_file, template, view, request

@route('/static/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./static/js')

@route('/static/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/img')

@route('/static/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/css')

@route("/")
@view("main")
def hello():
    return dict(title = "Sample Page")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='0.0.0.0', port=port, reloader=True, debug=True)
