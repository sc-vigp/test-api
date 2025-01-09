from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello/<input_name>', methods=['GET'])
def hello(input_name):
    return jsonify(message=f"Hello {input_name}")

if __name__ == '__main__':
    app.run(debug=True)