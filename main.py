from flask import Flask, redirect, request, url_for, jsonify


app = Flask(__name__)

@app.route('/api/name', methods=['GET'])  # <-- You need the @ symbol to decorate the function!
def api_name():
    name = "Anthony Dinunzio - Test"
    print('name: ', name)
    return jsonify({"message": name}), 200  # <-- The status code should be outside jsonify


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')