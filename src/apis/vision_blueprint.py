from sanic import Blueprint
from sanic.response import json

from src.apis.schemas.nlu import USER
from src.shared.utils.validators import validate_params

vision_blueprint = Blueprint("vision_blueprint", url_prefix="/api/v1/vision")


@vision_blueprint.route("/test", methods=["POST"])
@validate_params(USER)
async def test(request):
    data = request.json
    return json(
        {
            "message": f"Hello, {data['name']}! Your email is {data['email']} and you are {data['age']} years old."
        }
    )
