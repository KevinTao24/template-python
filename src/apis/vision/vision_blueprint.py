from sanic import Blueprint
from sanic.response import json

from src.apis.vision.vision_schema import USER
from src.shared.utils.logger import setup_logger
from src.shared.utils.validators import validate_params

vision_blueprint = Blueprint("vision_blueprint", url_prefix="/api/v1/vision")

logger = setup_logger(__name__, log_level="INFO", log_file="template.log")


@vision_blueprint.route("/test", methods=["POST"])
@validate_params(USER)
async def test(request):
    data = request.json
    logger.info("hello debug")
    return json(
        {
            "message": f"Hello, {data['name']}! Your email is {data['email']} and you are {data['age']} years old."
        }
    )
