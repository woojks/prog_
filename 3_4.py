#A

for index, word in enumerate(input().split(), start=1):
    print(f'{index}. {word}')


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
num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
mast = ['пик', 'треф', 'бубен', 'червей']
mast.remove(input())
for n, m in product(num, mast):
    print(n, m)


#G

from itertools import combinations
names = [input() for _ in range(int(input()))]
print('\n'.join([f'{name1} - {name2}' for name1, name2 in list(combinations(names, 2))]))  

задача #H

from itertools import islice, cycle
kasha = [input() for _ in range(int(input()))]
kdays = int(input())
menu = islice(cycle(kasha), kdays)
print('\n'.join(menu))

#I

import itertools
n = int(input())
num = range(1, n + 1)
tab = [x * y for x, y in itertools.product(num, repeat=2)]
for i in range(n):
    print(*itertools.islice(tab, i * n, (i + 1) * n))

#J

from itertools import combinations
dol = int(input())
num = range(1, dol)
print('А Б В')
for fst, snd in list(combinations(num, 2)):
    print(f'{fst} {snd - fst} {dol - snd}')
