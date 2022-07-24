from flask import Flask, jsonify

"""
This is the server of quizlet web app
"""
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return 'pong'


if __name__ == '__main__':
    app.run()
