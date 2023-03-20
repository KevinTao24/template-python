from dataclasses import dataclass
from typing import Dict, Optional, Text

from pydantic import BaseModel, Field


@dataclass
class TestBody(BaseModel):
    senderId: Text = Field(
        title="senderId",
        description="单次请求唯一ID",
        example="test001",
        required=True,
    )
    name: Text
    email: Optional[Text]
    age: int = 24


class TestResponse(BaseModel):
    code: int = Field(
        title="code",
        description="响应码",
        example=200,
        required=True,
    )
    success: bool = Field(
        title="success",
        description="是否成功返回",
        example=True,
        required=True,
    )
    message: Text = Field(
        title="message",
        description="返回信息内容",
        example="response success",
        required=True,
    )
    requestId: Text = Field(
        title="requestId",
        description="单次请求唯一ID",
        example="test001",
        required=True,
    )
    data: Dict = Field(
        title="data",
        description="返回结果内容",
        example={},
        required=True,
    )
