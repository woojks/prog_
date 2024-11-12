# (задача #A)

print('Как Вас зовут? ')
name = input()
print(f'Здравствуйте, {name}!')
print('Как дела? ')
mood = input()
if mood == 'хорошо':
    print('Я за вас рада!')
if mood == 'плохо':
    print('Всё наладится!')


# (задача #B)

petya = int(input())
vasya = int(input())
if vasya > petya:
    print('Вася')
elif petya > vasya:
    print('Петя')

# (задача #C)

petya = int(input())
vasya = int(input())
tolya = int(input())
if vasya > petya and vasya > tolya:
    print('Вася')
elif petya > vasya and petya > tolya:
    print('Петя')
elif tolya > vasya and tolya > petya:
    print('Толя')
else:
    print('непонятно')


# (задача #D)

petya = int(input())
vasya = int(input())
tolya = int(input())

if vasya > petya > tolya:
    print('1. Вася')
    print('2. Петя')
    print('3. Толя')
elif vasya > tolya > petya:
    print('1. Вася')
    print('2. Толя')
    print('3. Петя')
elif petya > vasya > tolya:
    print('1. Петя')
    print('2. Вася')
    print('3. Толя')
elif petya > tolya > vasya:
    print('1. Петя')
    print('2. Толя')
    print('3. Вася')
elif tolya > petya > vasya:
    print('1. Толя')
    print('2. Петя')
    print('3. Вася')
elif tolya > vasya > petya:
    print('1. Толя')
    print('2. Вася')
    print('3. Петя')

# (задача #E)

petya = 7
vasya = 6
n_apples = int(input())
m_apples = int(input())
petya = petya - 3 + 2 + n_apples
vasya = vasya + 3 + 5 - 2 + m_apples
if petya > vasya:
    print('Петя')
elif vasya > petya:
    print('Вася')


# (задача #F)

year = int(input())
yes = False
if year % 400 == 0:
    yes = True
elif year % 100 == 0:
    yes = False
elif year % 4 == 0:
    yes = True
else:
    yes = False
if yes:
    print('YES')
else:
    print('NO')


# (задача #G)

num = int(input())
if num // 1000 == num % 10 and num % 1000 // 100 == num % 100 // 10:
    print('YES')
else:
    print('NO')


# (задача #H)

nature = input()
if 'зайка' in nature:
    print('YES')
else:
    print('NO')

# (задача #I)

first = input()
second = input()
third = input()
if first < second and first < third:
    print(first)
elif second < first and second < third:
    print(second)
elif third < first and third < second:
    print(third)

# (задача #J)

num = int(input())
first = num // 10
last = num % 100
sum1 = first // 10 + first % 10
sum2 = last // 10 + last % 10
if sum1 < sum2:
    print(str(sum2) + str(sum1))
else:
    print(str(sum1) + str(sum2))
