import pkg_resources
from sanic import Blueprint
from sanic.response import json
from sanic_ext import validate

from src.apis.nlu.nlu_schema import TestBody

nlu_blueprint = Blueprint("nlu_blueprint", url_prefix="/api/v1/nlu")

test_create_doc = pkg_resources.resource_string(
    __name__, "../../../docs/nlu/test.yaml"
).decode("utf-8")


@nlu_blueprint.route("/test", methods=["POST"])
@validate(json=TestBody)
async def test(request, body: TestBody):
    """This is a simple test demo."""

    return json(
        {
            "message": f"Hello, {body.name}! Your email is {body.email} and you are {body.age} years old."
        }
    )
