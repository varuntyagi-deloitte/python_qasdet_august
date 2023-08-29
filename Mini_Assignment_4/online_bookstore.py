'''Online BookStore'''
from functools import reduce

books = ["Book1", "Book2", "Book3", "Book4", "Book5"]

prices = [39.99, 54.99, 49.99, 49.99, 44.99]

dict_1 = dict(zip(books, prices))
result_1 = []
result = list(filter(lambda price: price > 50.00, prices))
for i, j in dict_1.items():
    if dict_1.get(i) in result:
        result_1.append(i)
print('Filtered Books:', result_1)
result_3 = reduce(lambda x, y: x + y, result)
print('Total Revenue', result_3)
print('Book-Price Tuples:', list(zip(result_1, result)))