#A

print('\n'.join([f'{index}. {value}' for index, value in enumerate(input().split(), 1)]))

#B

left = input().split(', ')
right = input().split(', ')
for kids in zip(left, right):
    print(f'{kids[0]} - {kids[1]}')

#C

from itertools import count
start, stop, step = [float(x) for x in input().split()]
for num in count(start, step):
    if num >= stop:
        break
    print(f'{num:.2f}')

#D

from itertools import accumulate
print('\n'.join(list(accumulate([word + ' ' for word in input().split()]))))


#E

from itertools import chain
lst = sorted(set(chain.from_iterable([input().split(", ") for _ in range(3)])))
for index, value in enumerate(lst, 1):
    print(f"{index}. {value}")

#F

from itertools import product
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']
suits.remove(input())
for card, suit in product(cards, suits):
    print(card, suit)


#G

from itertools import combinations
names = [input() for _ in range(int(input()))]
print('\n'.join([f'{name1} - {name2}' for name1, name2 in list(combinations(names, 2))]))  

задача #H

from itertools import cycle, islice
porridges = [input() for _ in range(int(input()))]
days = int(input())
print('\n'.join(islice(cycle(porridges), days)))

#I

from itertools import product, islice
size = int(input())
nums = range(1, size + 1)
table = [x * y for x, y in product(nums, repeat=2)]
for row in range(size):
    print(*islice(table, row * size, (row + 1) * size))

#J

from itertools import product
num = int(input())
nums = range(1, num - 1)
table = list(product(nums, repeat=3))
print('А Б В')
for i in range(len(table)):
    if sum(table[i]) == num:
        print(*table[i])