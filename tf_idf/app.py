import os

from flask import Flask

from .config.routes import routes

app = Flask(__name__)

routes(app)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
