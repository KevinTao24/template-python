from sanic import Blueprint
from sanic.response import json
from sanic_ext import openapi, validate

from src.apis.nlu.nlu_schema import TestBody, TestResponse

nlu_blueprint = Blueprint("nlu_blueprint", url_prefix="/api/v1/nlu")


@nlu_blueprint.route("/test", methods=["POST"])
@openapi.definition(
    body={"application/json": TestBody.schema()},
    tag="nlu_blueprint",
    summary="api/v1/nlu/test",
    response=[
        openapi.definitions.Response(
            {"application/json": TestResponse.schema()}, 200, "Success"
        ),
        openapi.definitions.Response(
            {"application/json": TestResponse.schema()}, 400, "Failure"
        ),
    ],
)
@validate(json=TestBody)
async def test(request, body: TestBody):
    return json(
        {
            "message": f"Hello, {body.name}! Your email is {body.email} and you are {body.age} years old."
        }
    )


@nlu_blueprint.route("/test2", methods=["POST"])
@openapi.definition(
    body={"application/json": TestBody.schema()},
    tag="nlu_blueprint",
    summary="api/v1/nlu/test2",
    response=[
        openapi.definitions.Response(
            {"application/json": TestResponse.schema()}, 200, "Success"
        ),
    ],
)
@validate(json=TestBody)
async def test2(request, body: TestBody):
    return json(
        {
            "message": f"Hello, {body.name}! Your email is {body.email} and you are {body.age} years old."
        }
    )
