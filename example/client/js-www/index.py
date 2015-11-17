#!/usr/bin/env python
###############################################################################

from bottle import Bottle, run, static_file

###############################################################################

app = Bottle()

###############################################################################

@app.route('/')
@app.route('/<file:path>')
def static_serve(file='index.html'):
    return static_file(file, root='.')

###############################################################################

run(app, host='localhost', port=8080)

###############################################################################
