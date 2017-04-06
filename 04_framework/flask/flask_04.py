from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/login', methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		error = request.cookies.get('username')
	else:
		error = 'Invalid username/password'
	return render_template('login.html',error=error)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404

app.logger.debug('debug')

if __name__ == "__main__":
	app.run(host="localhost", port=5000)