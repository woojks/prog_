#A

def make_list(length, value=0):
    return [value for _ in range(length)]

#B

def make_matrix(size, value=0):
    if isinstance(size, int):
        size = [size, size]
    result = [[value] * size[0] for _ in range(size[1])]
    return result


#C

def gcd(*numbers):
    a, *tail = numbers
    for b in tail:
        while b:
            a, b = b, a % b
    return a


#D

def month(num, lang='ru'):
    MONTHS = {
        'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
               'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
             }

    return MONTHS[lang][num - 1]


 #E


def to_string(*data, sep=' ', end='\n'):
    return sep.join(str(item) for item in data) + end