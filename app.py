import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

response_sampe = {"Application":"Cache0",
     "Version":"0.2.0",
     "Uptime":4029194611,
     "Request_Count":1722952160,
     "Error_Count":905551894,
     "Success_Count":817400266}

status = [
    {"status": "OK"}
]

@app.route("/", methods=['GET'])
def home():
    return "<h1>Welcome to the server status report application!</h1>"


@app.route("/health")
def health():
    return jsonify(status)

@app.route('/status', methods=['GET'])
def api_server():
    return jsonify(response_sampe)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    app.run(debug=True)
