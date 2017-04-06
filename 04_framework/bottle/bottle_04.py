from bottle import route, install, template, run
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='../../db/test.db'))

@route('/show/<post_id:int>')
def show(db, post_id):
    c = db.execute('SELECT title, content FROM posts WHERE id = ?', (post_id,))
    row = c.fetchone()
    return template('show_post', title=row['title'], text=row['content'])

# http://localhost:3000/contact\
@route('/contact')
def contact_page():
    ''' This callback does not need a db connection. Because the 'db'
        keyword argument is missing, the sqlite plugin ignores this callback
        completely. '''
    return template('contact')

run(reloader=True, host='localhost', port=3000, debug=True)