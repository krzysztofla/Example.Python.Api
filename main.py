import json
import logging
from flask import request
from flask import Flask


app = Flask(__name__)
app.run(debug=True, port=8080, host="localhost")

@app.route("/")
def HelloWorld():
    logging.debug(request.host)
    logging.debug(request.data)
    print(request.host)
    print(request.host_url)
    print(request.data)
    return request.host