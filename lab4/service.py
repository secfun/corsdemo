from flask import request
import json
from flask import Flask
from flask import render_template
import time
from flask import make_response

app = Flask(__name__)

safe_counter = 0
@app.route('/safe_counter/', methods=['GET', 'POST'])
def safe_counter_view():
    global safe_counter
    if request.method == 'POST':
        csrftoken_form = request.values.get("csrftoken")
        csrftoken_cookie = request.cookies.get('csrftoken')
        if csrftoken_form != csrftoken_cookie:
            return 'unauth', 403
        safe_counter += 1

    return str(safe_counter)


@app.route('/index/', methods=['GET', 'POST'])
def index():
    token = str(int(time.time()))
    response = make_response(render_template('index.html', csrftoken=token))
    response.set_cookie('csrftoken', token)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9093')

