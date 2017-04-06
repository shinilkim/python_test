# http://bottlepy.org/docs/dev/tutorial_app.html#server-setup

from bottle import route, run, template

@route('/hello')
def hello():
    return "Hello World!"

@route('/hello/<name>/<age>')
def hello2(name, age):
    return "Hello, "+name+"("+age+")"

@route('/h')
@route('/h/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/object/<id:int>')
def obj(id):
    return id

@route('/show/<name:re:[a-z]+>')
def show(name):
    return name.isalpha()

run(host='localhost', port=3000, debug=True)