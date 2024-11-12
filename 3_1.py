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


string = input()
lst = string.split()
print(int(lst[0]) + int(lst[1]))

# (задача #H)


count = int(input())
for _ in range(count):
    string = input()
    if 'зайка' in string:
        print(string.index('зайка') + 1)
    else:
        print("Заек нет =(")


# (задача #I)


while string := input():
    if not (pos := string.find('#')) + 1:
        print(string)
    elif string[:pos].strip():
        print(string[:pos].rstrip())


# (задача #J)


text = ''
while (string := input()) != 'ФИНИШ':
    text += string.lower()
text = text.replace(' ', '')
seen = ''
maximum = 0
most_frequent_char = ''
for char in text:
    if char not in seen:
        seen += char
        count = text.count(char)
        if count > maximum:
            maximum = count
            most_frequent_char = char
        elif count == maximum:
            if char < most_frequent_char:
                most_frequent_char = char
print(most_frequent_char.lower())