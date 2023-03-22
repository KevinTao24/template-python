import os
import sys

sys.path.insert(-1, os.getcwd())

from sanic import Sanic
from sanic.response import json
from sanic_ext import Extend

from src.apis.nlu.nlu_blueprint import nlu_blueprint
from src.apis.vision.vision_blueprint import vision_blueprint
from src.core.nlu.tokenizers.jieba_tokenizer import JiebaTokenizer
from src.shared.utils.logger import setup_logger

app = Sanic(__name__)
app.blueprint(nlu_blueprint)
app.blueprint(vision_blueprint)

Extend(app)

logger = setup_logger("main", log_file="template.log")

tokenizer = JiebaTokenizer()


@app.route("/health", methods=["GET"])
async def health_check(request):
    result = {}
    tokens = tokenizer.process("江苏省南京市高淳区")
    result["text_tokens"] = [token.to_dict() for token in tokens]
    return json(result)


@app.middleware("request")
async def log_request(request):
    logger.info(f"Request: {request.ip} {request.method} {request.path}")


@app.middleware("response")
async def log_response(request, response):
    logger.info(f"Response: {response.status} {len(response.body)}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
