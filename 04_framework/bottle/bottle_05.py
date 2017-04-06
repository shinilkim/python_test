import bottle
app = bottle.default_app()             # or bottle.Bottle() if you prefer

app.config['autojson']    = False      # Turns off the "autojson" feature
app.config['sqlite.db']   = ':memory:' # Tells the sqlite plugin which db to use
app.config['myapp.param'] = 'value'    # Example for a custom config value.

# Change many values at once
app.config.update({
    'autojson': False,
    'sqlite.db': ':memory:',
    'myapp.param': 'value'
})

# Add default values
app.config.setdefault('myapp.param2', 'some default')

# Receive values
param  = app.config['myapp.param']
param2 = app.config.get('myapp.param2', 'fallback value')

# An example route using configuration values
@app.route('/about', view='about.rst')
def about():
    email = app.config.get('my.email', 'nomail@example.com')
    return {'email': email}

@app.route('/about2')
def is_admin():
    return bottle.request.app.config['myapp.admin_user']

@app.route('/about3')
def about3():
    param = {
        'sqlite' : {
            'db'     : app.config['sqlite.db'],
            'commit' : app.config['sqlite.commit']
        },
        'myapp' : {
            'admin_user' : app.config['myapp.admin_user']
        }
    }
    return param


app.config.load_config('../../config/test/bottle.conf')

bottle.run(host='localhost', port=3000, debug=True)