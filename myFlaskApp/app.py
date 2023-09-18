
from flask import Flask
from decouple import config
import os;


app = Flask(__name__)
# Access environment variables directly
loginKey= os.environ.get('login')

@app.route('/')
def hello():
    return 'Hello, Flask!'


@app.route("/logout")
def login():
    return {"key":loginKey}







if __name__ == '__main__':
    app.run(debug=False)

