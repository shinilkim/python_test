from bottle import run, get, post, request, response, static_file, error, route, abort, template, view

# http://localhost:3000/login
@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    return True

# http://localhost:3000/static2/bottle_01.py
@get('/static/<filename>')
@get('/static2/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./')

# http://localhost:3000/iso?name=abc_123_김신일
@route('/iso')
def get_iso():
    a = request.query['name']
    b = request.query.name
    #response.charset = 'ISO-8859-15'
    return u'This will be sent with ISO-8859-15 encoding {%s : %s}' % (a,b)

# http://localhost:3000/counter
@route('/counter')
def counter():
    count = int( request.cookies.get('counter', '0') )
    count += 1
    response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count

# http://localhost:3000/is_ajax
@route('/is_ajax')
def is_ajax():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return 'This is an AJAX request'
    else:
        return 'This is a normal request'

# http://localhost:3000/latin9
@route('/latin9')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return u'ISO-8859-15 is also known as latin9.'

@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='/path/to/image/files', mimetype='image/png')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/path/to/static/files')

# http://localhost:3000/download/bottle_01.py
@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='./', download=filename)

# http://localhost:3000/forum?id=shinil.kim
@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)

# http://localhost:3000/my_ip
@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)

@route('/hello3')
@route('/hello3/<name>')
@view('template/hello_template.html')
def hello(name='World'):
    return dict(name=name)

# http://localhost:3000/hello2
@route('/hello2')
def hello_again():
    name = request.cookies.name
    #name = request.cookies.getunicode('name')  # encoding='utf-8' (default)
    if name == None:
        name = 'shinil.kim'
    response.set_cookie('name',name)
    try:
        name = name
        #name = request.cookies.get('name', '').decode('utf-8')
    except UnicodeError:
        name = u''

    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again ~ "+name
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you ~ "+name



#######################
@error(404)
def error_404(error):
    return 'Nothing here, sorry: '

# http://localhost:3000/restricted
@route('/restricted')
def restricted():
    name = request.cookies.username or 'Guest'
    response.set_header('Set-Cookie', 'name='+name)
    response.add_header('Set-Cookie', 'name2=value2')
    response.set_header('Content-Language', 'en')
    abort(401, "Sorry, access denied.")

run(host='localhost', port=3000, debug=True)