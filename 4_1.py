#A

def print_hello(name):
    print(f'Hello, {name}!')

#B

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#C


def number_length(number):
    return len(str(abs(number)))


#D


def month(num, lang):
    MONTHS = {
        'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
               'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
             }

    return MONTHS[lang][num - 1]

#E

def split_numbers(string):
    return tuple([int(number) for number in string.split()])