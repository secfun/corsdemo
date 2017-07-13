from flask import request
import json
from flask import Flask
app = Flask(__name__)

counter = 0
@app.route('/counter/', methods=['GET', 'POST'])
def counter():
    global counter
    if request.method == 'POST':
        counter += 1

    return str(counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9093')

