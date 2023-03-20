from sanic import Blueprint
from sanic.response import json
from sanic_ext import validate

from src.apis.vision.vision_schema import TestBody
from src.shared.utils.logger import setup_logger

vision_blueprint = Blueprint("vision_blueprint", url_prefix="/api/v1/vision")

logger = setup_logger(__name__, log_level="INFO", log_file="template.log")


@vision_blueprint.route("/test", methods=["POST"])
@validate(json=TestBody)
async def test(request, body: TestBody):
    """This is a simple test demo."""

    return json(
        {
            "message": f"Hello, {body.name}! Your email is {body.email} and you are {body.age} years old."
        }
    )
