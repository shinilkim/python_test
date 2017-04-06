# https://pypi.python.org/pypi/Flask/0.12
# pip install Flask
from flask import Flask
app = Flask(__name__)

# localhost:5000
@app.route("/")
def hello():
	return "Hello World!"

# localhost:5000/user/shinil.kim
@app.route("/user/<userName>")
def show_user_profile(userName):
	return "User %s" %(userName)

# localhost:5000/post/123
 # string, int, float, path, any, uuid
@app.route("/post/<int:post_id>")
def show_post(post_id):
	return "Post %d" % post_id

if __name__ == "__main__":
	app.run(host="localhost", port=5000)