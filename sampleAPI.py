from flask import Flask, request, jsonify

app = Flask(__name__)

from waitress import serve
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

#get accesses the content of the server
@app.route('/get', methods=['GET'])
def testGet():
    return jsonify('message','test works')

#post adds something to the server
@app.route('/post', methods=['POST'])
def testPost():
    data = request.json
    print(data)
    return 'POST works'

@app.route('/')
def is_up():
    return 'Server is up'

if __name__ == '__main__':
    #app.run(host = '0.0.0.0', port = 80880, debug=True)
    serve(app, host='0.0.0.0', port=8080)
