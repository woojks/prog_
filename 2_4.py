
dim = int(input())
for i in range(dim):
    for j in range(dim):
        print((i + 1) * (j + 1), end=' ')
    print()
# задача A


dim = int(input())
for i in range(1, dim + 1):
    for j in range(1, dim + 1):
        print(f'{j} * {i} = {i * j}')
# задача B 


dim = int(input())
count = 1
num = 1
while num <= dim:
    for i in range(count):
        if num > dim:
            break
        print(num, end=' ')
        num += 1
    print()
    count += 1
# задача C



count = int(input())
summa = 0
for _ in range(count):
    number = int(input())
    while number > 0:
        summa += number % 10
        number //= 10
print(summa)
# задача D


natures = int(input())
bunnies = 0
for _ in range(natures):
    counted = False
    while (s := input()) != 'ВСЁ':
        if s == 'зайка' and counted is False:
            bunnies = bunnies + 1
            counted = True
print(bunnies)
# задача E



count = int(input())
gcd = int(input())
for _ in range(count - 1):
    number = int(input())
    while number != 0 and gcd != 0:
        if number >= gcd:
            number %= gcd
        else:
            gcd %= number
    gcd = gcd + number
print(gcd)

# задача F



count = int(input())
base_delay = 3
for number in range(1, count + 1):
    for delay in range(base_delay):
        print('До старта', base_delay - delay, 'секунд(ы)')
    print(f'Старт {number}!!!')
    base_delay += 1
# задача G



count = int(input())
best_name = ''
best_sum = 0
for i in range(count):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if summa >= best_sum:
        best_sum = summa
        best_name = name
print(best_name)

# задача H





count = int(input())
result = 0
for _ in range(count):
    number = int(input())
    maximum = -1
    while number > 0:
        if number % 10 > maximum:
            maximum = number % 10
        number //= 10
    result = result * 10 + maximum
print(result)
# задача I




slices = int(input())
print('А Б В')
for a in range(1, slices - 1):
    for b in range(1, slices - a):
        c = slices - a - b
        print(a, b, c)
        # задача J