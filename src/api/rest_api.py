from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from kafka_utils.producer import producer_msg

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)

@app.route('/protected')
@basic_auth.required
def protected():
    return 'This page is protected by basic authentication'

@app.route('/create/<string:source>', methods=['POST'])
@basic_auth.required
def receive_new_data(source):
    data = request.get_json()
    if len(data) > 0:
        for d in data:
            try:
                producer_msg(d, source)
                return jsonify({'message': 'Data received successfully'})
            except KeyError as e:
                producer_msg(d, 'errors')
                return jsonify({'message': 'Transactions are not valid due to typo rules.'})
    else:
        return jsonify({'message': 'Invalid format'}) 