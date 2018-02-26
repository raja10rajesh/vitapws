from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/hello")

def hello():
        return jsonify({
             'message':'madhav likes icecreams',
             'status_code':200
                })
	
if __name__ == '__main__':
	app.run(debug=True)
