import os
from typing import List, Text

import jieba

from src.core.nlu.tokenizers.tokenizer import Token, Tokenizer
from src.shared.utils.logger import setup_logger

logger = setup_logger(__name__, log_file="template.log")


class JiebaTokenizer(Tokenizer):
    default = {
        "dictionary_path": os.getcwd() + "/src/core/nlu/tokenizers/jieba_userdict.txt",
    }

    def __init__(self, dictionary_path: Text = default["dictionary_path"]) -> None:
        """Initialize the tokenizer."""

        if dictionary_path:
            logger.info(f"Loading Jieba User Dictionary at {dictionary_path}")
            jieba.load_userdict(dictionary_path)

    def tokenize(self, text: Text) -> List[Token]:
        """Tokenizes the text of the provided."""

        tokenized = jieba.tokenize(text)
        tokens = [Token(word, start, end) for (word, start, end) in tokenized]

        return tokens
