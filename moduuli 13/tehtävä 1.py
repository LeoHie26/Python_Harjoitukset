from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):

    result = {
        'Number': number,
        'isPrime': is_prime(number)
    }

    return jsonify(result)

if __name__ =='__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)