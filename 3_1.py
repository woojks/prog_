# (задача #A)

n = int(input())
for _ in range(n):
    n -= input()[0].lower() in 'абв'
print('YES' if not n else 'NO')


# (задача #B)

string = input()
for letter in string:
    print(letter)

# (задача #C)

length = int(input())
count = int(input())
for _ in range(count):
    string = input()
    if len(string) <= length:
        print(string)
    else:
        print(f'{string[:length - 3]}...')

# (задача #D)

while string := input():
    if not string.endswith('@@@'):
        if string.startswith('##'):
            string = string[2:]
        print(string)

# (задача #E)

string = input()
if string == string[::-1]:
    print('YES')
else:
    print('NO')


# (задача #F)

count = int(input())
bunnies = 0
for _ in range(count):
    string = input()
    bunnies += string.count('зайка')
print(bunnies)


# (задача #G)

n = input()
lst = n.split()
print(int(lst[0]) + int(lst[1]))

# (задача #H)

n = int(input())
for _ in range(n):
    text = input()
    counter = text.find('зайка') + 1
    if counter:
        print(counter)
    else:
        print('Заек нет =(')


# (задача #I)

while text := input():
    if text.startswith('#'):
        continue
    if '#' in text:
        n = text.index('#')
        print(text[:n])
    else:
        print(text)


# (задача #J)

text = ''
n = input()
while n != 'ФИНИШ':
    text += n.lower()
    n = input()
counter = 0
maximum = ''
for i in text:
    if i == ' ':
        continue
    c = text.count(i)
    if c > counter:
        counter = c
        maximum = i
    elif c == counter:
        if i < maximum:
            maximum = i
print(maximum)
