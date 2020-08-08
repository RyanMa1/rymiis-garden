from flask import Flask, request, jsonify, render_template
import os, requests

app = Flask(__name__)

@app.route('/pi', methods=['POST'])
def main():
	print(request.get_json(force=True))
	return "200"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False, port = os.environ["PORT"])
