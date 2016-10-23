from flask import Flask
app = Flask(__name__)
from functools import wraps
from flask import request, abort
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('server.crt', 'server.key')

# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
        if request.args.get('key') and request.args.get('key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

@app.route('/json/', methods=['POST'])
@require_appkey
def put_user():
    return 'Posted JSON!'

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(host='127.0.0.1',port='443', debug = False/True, ssl_context=context)
