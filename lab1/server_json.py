from flask import request
import json
from flask import Flask
app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST'])
def counter():
    user = {"name": "xudy"}
    return json.dumps(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9092')

