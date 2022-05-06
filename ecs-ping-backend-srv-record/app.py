from flask import Flask
import os
import urllib.request
import json
import dns.resolver


app = Flask(__name__)
BACKEND_RECORD = str(os.getenv("BACKEND_RECORD"))

@app.route('/ping', methods=['GET'])
def healthcheck():
    return "ok"


@app.route('/', methods=['GET'])
def inc():
    data = {}
    answers = dns.resolver.query(BACKEND_RECORD, 'SRV')
    domain = ''
    port = ''
    for rdata in answers:
       domain = rdata.target
       port = rdata.port

    BACKEND_URL = "http://"+str(domain)+":"+str(port)
    backend_response = json.loads(urllib.request.urlopen(BACKEND_URL).read())
    data['backend_response'] = backend_response['response']
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
