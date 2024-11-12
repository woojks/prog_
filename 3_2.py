# (задача #A)


print(''.join(set(input())))



# (задача #B)


print(''.join(set(input()).intersection(set(input()))))


# (задача #C)


items = set()
for _ in range(int(input())):
    string = input()
    items |= set(string.split())  # items = items | set(string.split())
for item in items:
    print(item)


# (задача #D)


lilist1size = int(input())
list2size = int(input())
list1 = set()
list2 = set()
for _ in range(list1size):
    list1.add(input())
for _ in range(list2size):
    list2.add(input())
if len(junction := (list1 & list2)) != 0:
    print(len(junction))
else:
    print('Таких нет')


# (задача #E)


list1size = int(input())
list2size = int(input())
list1 = set()
list2 = set()
for _ in range(list1size + list2size):
    name = input()
    if name in list1:
        list2.add(name)
    else:
        list1.add(name)
# print(list1, list2)
if len(junction := (list1 ^ list2)) != 0:
    print(len(junction))
else:
    print('Таких нет')



# (задача #F)



list1size = int(input())
list2size = int(input())
list1 = set()
list2 = set()
for _ in range(list1size + list2size):
    eater = input()
    if eater in list1:
        list2.add(eater)
    else:
        list1.add(eater)
# print(list1, list2)
if len(junction := (list1 ^ list2)) != 0:
    for eater in sorted(junction):
        print(eater)
else:
    print('Таких нет')




# (задача #G)




MORZE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K':
         '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

for char in input():
    if char != ' ':
        print(MORZE[char.upper()], end=' ')
    else:
        print()



# (задача #H)


porridges_list = {}

for _ in range(int(input())):
    string = input()
    eater, *porridges = string.split()
    for porridge in porridges:
        porridges_list[porridge] = porridges_list.get(porridge, []) + [eater]

porridge = input()

if porridge in porridges_list:
    print('\n'.join(sorted(porridges_list[porridge])))
else:
    print('Таких нет')



# (задача #I)



objects = {}

while (string := input()) != '':
    words = string.split()
    for item in words:
        objects[item] = objects.get(item, 0) + 1

for item in objects:
    print(item, objects[item])



# (задача #J)



TRANSLITERATE_DICT = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}


result = ''

for char in input():
    char_copy = char.upper()
    if char_copy in TRANSLITERATE_DICT:
        if char.isupper():
            char = TRANSLITERATE_DICT[char_copy].capitalize()
        else:
            char = TRANSLITERATE_DICT[char_copy].lower()
    result += char
print(result)