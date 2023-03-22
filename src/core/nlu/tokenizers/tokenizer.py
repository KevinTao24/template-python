import abc
from typing import List, Optional, Text


class Token:
    def __init__(
        self,
        text: Text,
        start: int,
        end: Optional[int] = None,
    ) -> None:
        """Create a `Token`.

        Args:
            text: The token text.
            start: The start index of the token within the entire message.
            end: The end index of the token within the entire message.
        """
        self.text = text
        self.start = start
        self.end = end if end else start + len(text)

    def to_dict(self):
        return {"text": self.text, "start": self.start, "end": self.end}


class Tokenizer(abc.ABC):
    @abc.abstractmethod
    def tokenize(self, text: Text) -> List[Token]:
        """Tokenizes the text of the provided."""
        ...

    def process(self, text: Text) -> List[Token]:
        """Tokenize the incoming messages."""

        tokens = self.tokenize(text)

        return tokens
