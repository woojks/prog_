# A


text = set(input())
for i in text:
    print(i, end='')

# B

fst = set(input())
snd = set(input())
for i in fst & snd:
    print(i, end='')


# C

n = set()
textnum = int(input())
for _ in range(textnum):
    text = input()
    n = n | set(text.split())
for i in n:
    print(i)

# D

n = int(input())
m = int(input())
listn = set()
listm = set()
for _ in range(n):
    listn.add(input())
for _ in range(m):
    listm.add(input())
if len(itog := (listn & listm)) != 0:
    print(len(itog))
else:
    print('Таких нет')

# E

manCH = int(input())
ovsCH = int(input())
surnames = set()
for _ in range(manCH + ovsCH):
    surname = input()
    if surname in surnames:
        surnames.remove(surname)
    else:
        surnames.add(surname)
if surnames:
    print(len(surnames))
else:
    print('Таких нет')

# F

manCH = int(input())
ovsCH = int(input())
surnames = set()
for _ in range(manCH + ovsCH):
    surname = input()
    if surname in surnames:
        surnames.remove(surname)
    else:
        surnames.add(surname)
if len(surnames) != 0:
    for surname in sorted(surnames):
        print(surname)
else:
    print('Таких нет')


# G

dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.', 
              'G': '--.', 'H': '....', 'I': '..', 
              'J': '.---', 'K': '-.-', 'L': '.-..', 
              'M': '--', 'N': '-.', 'O': '---', 
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 
              'S': '...', 'T': '-', 'U': '..-', 
              'V': '...-', 'W': '.--', 'X': '-..-', 
              'Y': '-.--', 'Z': '--..', '0': '-----', 
              '1': '.----', '2': '..---', '3': '...--', 
              '4': '....-', '5': '.....', '6': '-....', 
              '7': '--...', '8': '---..', '9': '----.'}
for i in input():
    if i != ' ':
        print(dictionary[i.upper()], end=' ')
    else:
        print()


# H

slr = dict()
for _ in range(int(input())):
    spisok = input().split()
    name = spisok[0]
    kasha = spisok[1:]
    for i in kasha:
        if i not in slr:
            slr[i] = [name]
        else:
            slr[i].append(name)
key = input()
if key in slr:
    print("\n".join(sorted(slr[key])))
else:
    print("Таких нет")

# I

mesto = dict()
while (text := input()) != '':
    animals = text.split()
    for animal in animals:
        if animal in mesto:
            mesto[animal] += 1
        else:
            mesto[animal] = 1
for animal in mesto:
    print(animal, mesto[animal])



# J

translit = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 
            'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 
            'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 
            'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 
            'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 
            'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''}
itog = ''
for vse in input():
    VSE = vse.upper()
    if VSE in translit:
        if vse.isupper():
            vse = translit[VSE].capitalize()
        else:
            vse = translit[VSE].lower()
    itog += vse
print(itog)
