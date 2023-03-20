import os
import sys

sys.path.insert(-1, os.getcwd())

from sanic import Sanic

from src.apis.nlu_blueprint import nlu_blueprint
from src.apis.vision_blueprint import vision_blueprint

app = Sanic(__name__)
app.blueprint(nlu_blueprint)
app.blueprint(vision_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
