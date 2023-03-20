from dataclasses import dataclass
from typing import Optional, Text


@dataclass
class TestBody:
    senderId: Text
    name: Text
    email: Optional[Text]
    age: int = 24
