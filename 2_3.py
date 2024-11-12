# (задача #A)


s = input()
while s != 'Три!':
    print('Режим ожидания...')
    s = input()
print('Ёлочка, гори!')


# (задача #B)


count = 0
while (s := input()) != 'Приехали!':
    if 'зайка' in s:
        count += 1
print(count)


# (задача #C)


start, stop = int(input()), int(input())
for i in range(start, stop + 1):
    print(i, end=' ')


# (задача #D)


start, stop = int(input()), int(input())
if stop >= start:
    for i in range(start, stop + 1):
        print(i, end=' ')
else:
    for i in range(start, stop - 1, -1):
        print(i, end=' ')


# (задача #E)


summa = 0
while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    summa += price
print(summa)


# (задача #F)


a, b = int(input()), int(input())
while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a
print(a + b)


# (задача #G)


a, b = a1, b1 = int(input()), int(input())
while a != 0:
    a, b = b % a, a
print(a1 * b1 // (a + b))


# (задача #H)


info = input()
repeat = int(input())
for _ in range(repeat):
    print(info)


# (задача #I)


num = int(input())
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)


# (задача #J)


x, y = 0, 0
while (direction := input()) != 'СТОП':
    n = int(input())
    if direction == 'ВОСТОК':
        x += n
    elif direction == 'ЗАПАД':
        x -= n
    elif direction == 'СЕВЕР':
        y += n
    elif direction == 'ЮГ':
        y -= n  
print(y)
print(x)