#importing Flask module
from flask import Flask, redirect, url_for
#defining application as Flask class of this app
app = Flask(__name__)

#this function will happen at the home page
@app.route('/')
#function that when calls says Hello World
def hello_world():
        return 'Hello World'

#this function will happen at xxxx/hello/sab
@app.route('/hello/<name>')
#function will say hello and then name in URL
def hello_name(name):
        return 'Hello %s!' % name

#this function will happen at xxx/user/sab
@app.route('/user/<user>')
#if <user> is Sab it'll say I'm the best otherwise something else
def hello_user(user):
    if user == 'Sabrina':
        return 'You are the best person in the world'
    else:
        return redirect(url_for('hello_name', name = user))

#app will run when __name__ = __main__ which happens when this file is run
if __name__ == '__main__':
    app.run()

