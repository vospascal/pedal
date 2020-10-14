# names = ['a', 'b', 'c']
# for index, name in enumerate(names, start=1):
#     print (index, name)
## result
## 1 a
## 2 b
## 3 c


# names = ['a', 'b', 'c']
# numbers = [1, 2, 3]
# for name, number in zip(names, numbers):
#     print(f'{name} is number {number}')
## result
## a is number 1
## b is number 2
## c is number 3

# tuple
# items = (1, 2)
# a, b = items
# print(f'{a} and {b}')
## result 1 and 2

# items = (1, 2, 3, 4, 5, 6)
# a, b, *_ = items
# print(f'{a} and {b}')
## result 1 and 2


# items = (1, 2, 3, 4, 5, 6)
# a, b, *c , d = items
# print(f'{a} and {b} and {c}  and {d}')
## result 1 and 2 and [3, 4, 5]  and 6

