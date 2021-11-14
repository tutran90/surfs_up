from flask import Flask
# creating a new flask instance (singular version)
app = Flask(__name__)

#creating the first route (root)
@app.route('/')
def hello_world():
    return 'Hello world'

#SKILL DRILL Think of some simple code from which you could create a route. 
# Then try to create a new route implementing that logic.

@app.route('/index')
def index():
    return "Welcome to the Index"