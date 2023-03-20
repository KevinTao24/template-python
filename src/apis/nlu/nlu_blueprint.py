from sanic import Blueprint
from sanic.response import json

from src.apis.nlu.nlu_schema import USER
from src.shared.utils.validators import validate_params

nlu_blueprint = Blueprint("nlu_blueprint", url_prefix="/api/v1/nlu")


@nlu_blueprint.route("/test", methods=["POST"])
@validate_params(USER)
async def test(request):
    data = request.json
    return json(
        {
            "message": f"Hello, {data['name']}! Your email is {data['email']} and you are {data['age']} years old."
        }
    )
