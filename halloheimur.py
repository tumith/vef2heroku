#from bottle import route, run, template
from sys import argv

import bottle
from bottle import *

@route('/')
def index():
    return """
    <h2>Verkefni 1.</h2>
    <p><a href="/about">Tumi</a></p>
    <p><a href="/bio">The Mag</a></p>
    <p><a href="/pics">speigil</a></p>
    """

@route("/about")
def tumi():
    return "ÉG ER TUMI AHAHAHAHHAHHAHHAHAHAHAHHA"

@route("/bio")
def tumi():
    return "MEG ER HÁKARL"

@route("/pics")
def tumi():
    return "ÞETTA ER EKKI SPEIGIL EINGIN MYNDAVÉL"

bottle.run(host='0.0.0.0', port=argv[1])
#run(host='localhost' ,port='8060' debug=True)
