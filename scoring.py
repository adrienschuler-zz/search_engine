from math import sqrt, log


class Scoring:

    def term_frequency_normalized(
        term_frequency: int = 0,
        field_length: int = 1,
        avg_field_length: int = 1
    ) -> float:
        k1 = 1.2
        b = 0.75
        freq = term_frequency
        nominator = freq * (k1 + 1)
        denomiator = freq + k1 * 1 - b + b * field_length / avg_field_length
        return nominator / denomiator

    def inverted_document_frequency(
        documents_count: int = 1,
        document_frequency: int = 0
    ) -> float:
        return log(1 + (documents_count - document_frequency + 0.5) / (document_frequency + 0.5))

    def tfidf(
        term_frequency: int,
        field_length: int,
        avg_field_length: int,
        documents_count: int,
        document_frequency: int
    ) -> float:
        tf = Scoring.term_frequency_normalized(term_frequency, field_length, avg_field_length)
        idf = Scoring.inverted_document_frequency(documents_count, document_frequency)
        return round(tf * idf, 7)
