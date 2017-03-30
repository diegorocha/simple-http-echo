from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def echo(path):
    response = {}
    response['headers'] = dict(request.headers)
    response['args'] = dict(request.args)
    response['form'] = dict(request.form)
    return jsonify(response)


if __name__ == '__main__':
    app.run()
