from flask import Flask, render_template,jsonify
import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
import binascii


class Transactions:
    def __init__(self, sender_address, sender_private_key, recipient_address, value):
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value = value


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/make/transactions')
def make_transactions():
    return render_template("make_transactions.html")


@app.route('/view/transactions')
def view_transactions():
    return render_template("view_transactions.html")


@app.route('/wallet/new')
def new_wallet():
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()
    response = {
        'private_key': binascii.hexlify(private_key.export_key(format('DER'))).decode('ascii'),
        'public_key': binascii.hexlify(public_key.export_key(format('DER'))).decode('ascii')
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
