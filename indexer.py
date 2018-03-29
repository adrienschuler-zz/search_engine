from inverted_index import InvertedIndex
from tokenizer import Tokenizer


class Indexer():

    def __init__(self, inverted_index: InvertedIndex) -> None:
        self.inverted_index = inverted_index

    def index(self, doc_id: int, doc: str) -> None:
        for token in Tokenizer.whitespace(doc):
            self.inverted_index.add(doc_id, token)
