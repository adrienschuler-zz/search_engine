from operator import itemgetter

from scoring import Scoring


class InvertedIndex:

    def __init__(self) -> None:
        self.corpus = set()
        self.index = {}
        self.inverted_index = {}

    def clean(self, token: str) -> str:
        return token.lower()

    def get_avg_field_length(self):
        lengths = []
        for doc in self.index:
            lengths.append(len(doc))
        return sum(lengths) / float(len(lengths))

    def add(self, doc_id: str = None, token: str = ''):
        token = self.clean(token)

        if doc_id not in self.index:
            self.index[doc_id] = []

        self.index[doc_id].append(token)

        if token in self.inverted_index:
            if doc_id not in self.inverted_index[token]['postings']:
                self.inverted_index[token]['doc_freq'] += 1
                if 'postings' not in self.inverted_index[token]:
                    self.inverted_index[token]['postings'] = {}
                self.inverted_index[token]['postings'][doc_id] = 1
            else:
                self.inverted_index[token]['postings'][doc_id] += 1
        else:
            self.inverted_index[token] = {
                'doc_freq': 1,
                'postings': { doc_id: 1 }
            }

        self.corpus.add(doc_id)

        return self

    def get(self) -> dict:
        return self.inverted_index

    def size(self) -> int:
        return len(self.corpus)

    def match(self, token: str) -> dict:
        if token in self.inverted_index:
            return self.inverted_index[token]
        else:
            return None

    def search(self, token: str) -> dict:
        response = []
        match = self.match(token)
        if match:
            for doc_id, freq in match['postings'].items():
                field_length = len(self.index[doc_id])
                avg_field_length = self.get_avg_field_length()
                documents_count = self.size()
                document_frequency = match['doc_freq']
                score = Scoring.tfidf(freq, field_length, avg_field_length, documents_count, document_frequency)
                response.append({
                    'id': doc_id,
                    'doc': self.index[doc_id],
                    'score': score
                })
            return sorted(response, key=itemgetter('score'), reverse=True)
        else:
            return {}
