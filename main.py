from inverted_index import InvertedIndex
from indexer import Indexer

storage = InvertedIndex()
indexer = Indexer(storage)

indexer.index('1', 'The quick brown fox jumps over the lazy dog')
indexer.index('2', 'It is mostly comprised of nonsense phrases thought up by people who apparently find this sort of thing terribly clever')
indexer.index('3', 'there are remedies worse than the disease')
indexer.index('4', 'Do foxes carry disease? A fox bite is painful but offers less potential for infection than a domestic cat bite or scratch. Unless you are a wildlife rescuer fox bites are rare. However, it is always wise to seek antibiotic treatment for any animal bite, plus vaccination against tetanus.')
indexer.index('5', 'Fox News is an American basic cable and satellite television news channel owned by the Fox Entertainment Group, a subsidiary of 21st Century Fox.')
indexer.index('6', 'Lazy loading is a design pattern commonly used in computer programming to defer initialization of an object until the point at which it is needed. It can contribute to efficiency in the programs operation if properly and appropriately used. The opposite of lazy loading is eager loading.')
indexer.index('7', 'fox')
indexer.index('8', 'fox fox fox fox fox fox')

# print(storage.index)
# print(storage.inverted_index)

queries = ['fox', 'lazy', 'the', 'century']

for query in queries:
    results = storage.search(query)
    for result in results:
        print('query=%s\tid=%s\tscore=%f' % (query, result['id'], result['score']))
