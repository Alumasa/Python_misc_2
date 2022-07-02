#List Methods
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count("apple")
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)
fruits.reverse()
fruits
len(fruits)
fruits.append('grape')
fruits
len(fruits)
fruits.sort()
fruits
fruits.pop()
fruits

#Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack.pop()
stack.pop()
stack

#Lists as Queues
from collections import deque
from re import X
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Trevor")
queue.popleft()
queue.popleft()
queue

#List Comprehensions
#classic:
squares = []
for x in range(10):
    squares.append(x**2)

squares
x

#map,lambda:
squares = list(map(lambda x: x**2, range(10)))
squares
x

squares = [x**2 for x in range(10)]
squares

[(x, y) for x in (1, 2, 3) for y in (1, 3, 4) if x != y]

[(x, y) for x in (1, 2, 3) for y in (1, 3, 4)]

vec = [-1, -4, 0, 2, 4, -5, -3]
#double the list
[x*2 for x in vec]

#filter the list to exclude negative numbers
[x for x in vec if x >= 0]

#apply a function to all elements
[abs(x) for x in vec]

#call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

#create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

[x, x**2 for x in range(6)]

#flatten a list using listcomp with two 'for'
vec_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec_2 for num in elem]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]


#Nested List Comprehensions

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]
#transpose rows and columns
[[row[i] for row in matrix] for i in range(4)]

list(zip(*matrix))

#del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
del a[2:4]
a
del a[:]
a
del a
a