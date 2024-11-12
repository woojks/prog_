#A

from sys import stdin
summa = sum([int(num) for num in stdin.read().split()])
print(summa)

#B

from sys import stdin
delta = 0
strings = [line.rstrip('\n') for line in stdin.readlines()]
for string in strings:
    _, then, now = string.split()
    delta += int(now) - int(then)
print(round(delta / len(strings)))

#C

from sys import stdin
for string in stdin.readlines():
    if string == '\n':
        print(string)
    elif string.strip()[0] != '#':
        if (pos := string.find('# ')) + 1:
            string = string[:pos]
        print(string.strip('\n'))


#D


from sys import stdin
lines = stdin.readlines()
subject = lines[-1].strip('\n').lower()
objects = lines[:-1]
for line in objects:
    if line.lower().find(subject) + 1:
        print(line.strip('\n'))


#E


from sys import stdin
words = [word for word in stdin.read().split() if word]
result = [word for word in sorted(set(words)) if word.lower() == word[::-1].lower()]
print("\n".join(result))


#F


alphabet = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}

with open('transliteration.txt', 'w', encoding='UTF-8') as file_out:
    with open('cyrillic.txt', encoding='UTF-8') as file_in:
        for string in file_in:
            for char in string:
                current = char.upper()
                if current in alphabet:
                    if char.isupper():
                        char = alphabet[current].capitalize()
                    else:
                        char = alphabet[current].lower()
                else:
                    char = char
                print(char, end='', file=file_out)



#G


with open(input(), encoding='UTF-8') as file_in:
    numbers = [int(number) for number in file_in.read().split()]
print(length := len(numbers))
print(len([number for number in numbers if number > 0]))
print(min(numbers))
print(max(numbers))
print(total := sum(numbers))
print(f'{(total / length):.2f}')



#H


file_1 = input()
file_2 = input()
file_out = input()
with open(file_1, encoding='UTF-8') as file_in:
    items_1 = set([item for item in file_in.read().split()])
with open(file_2, encoding='UTF-8') as file_in:
    items_2 = set([item for item in file_in.read().split()])
unique = items_1 ^ items_2
with open(file_out, 'w', encoding='UTF-8') as file_name:
    print('\n'.join(sorted(unique)), file=file_name)



#I

file_in = input()
file_out = input()
with open(file_in, encoding="UTF-8") as file_in:
    text = file_in.read()
while text.find("\t") + 1:
    text = text.replace("\t", "")
while text.find("  ") + 1:
    text = text.replace("  ", " ")
text = "\n".join(string.strip() for string in text.split("\n") if string)
with open(file_out, "w", encoding="UTF-8") as file_out:
    file_out.write(text)


#J


file_name = input().strip()
lines = int(input())
with open(file_name, encoding='UTF-8') as file:
    data = [string for string in file.read().split('\n') if string]
print('\n'.join(data[-lines:]))