from flask import Flask, jsonify ,request

app = Flask(__name__)

users =[]

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    return jsonify({"username": username, "status": "Active"}), 200

@app.route('/user', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)