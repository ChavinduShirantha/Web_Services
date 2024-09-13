from flask import Flask, jsonify,request

app = Flask(__name__)

coins=[]

@app.route('/crypto', methods=['GET'])
def get_crypto():
    crypto = {
        "BTC": 48123.78,
        "ETH": 1710.45,
        "LTC": 298.56,
    }
    return jsonify(crypto), 200

@app.route('/savecrypto', methods=['POST'])
def create_crypto():
    coin = request.json
    coins.append(coin)
    return jsonify(coin), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)