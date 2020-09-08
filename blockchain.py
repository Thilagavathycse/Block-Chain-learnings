from flask import Flask,render_template
from time import time


class Blockchain:
    def __init__(self):
        self.transactions = []
        self.chain = []
        self.create_block(0, '00')

    def create_block(self, nonce, previous_hash):
        block = {
            'block_number': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.transactions,
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        self.transactions = []
        self.chain.append(block)



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
