from flask import Flask


app = Flask(__name__)


#decorator
@app.route('/')
def index():
    return 'Hello from Pet Adoption'


@app.route('/adopt_puppy')
def puppy():
    return 'Do you want to take me home with you?'



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')