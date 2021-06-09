import os
import sys
import json
from flask import Flask, jsonify, make_response, request, render_template

app = Flask("app_template")


# curl --location --request POST 'http://127.0.0.1:5000/data' \
# --header 'Content-Type: application/json' \
# --header 'Accept: application/json' \
# --header 'Application-Content: application/json' \
# --data-raw '{
#    "key": "val"
#

@app.route("/", methods=["GET"])
def index():
    return "homepage"


@app.route("/data", methods=["POST"])
def post_data():
    request_log = json.loads(json.dumps(request.json))
    sys.stdout.write(str(request_log) + '\n')

    return make_response(
        jsonify({
            "success": "true"
        }),
        200
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
