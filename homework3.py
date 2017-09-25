from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return 'main page'

@my_app.route('/2')
def second():
    return' secondary page'
@my_app.route('/3') 
def third():
    return 'third pages'

if __name__ == "__main__":
   my_app.debug = True
