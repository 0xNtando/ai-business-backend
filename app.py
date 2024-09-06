from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the AI Business Backend!"

@app.route('/wallets', methods=['GET'])
def get_wallets():
    # Placeholder for wallet data (you can expand this later)
    wallets = [
        {"id": 1, "address": "0x123...", "balance": 10.5},
        {"id": 2, "address": "0x456...", "balance": 7.8}
    ]
    return jsonify(wallets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
