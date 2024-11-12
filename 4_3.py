#A

def recursive_sum(*nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(*nums[1:])   


#B

def recursive_digit_sum(num):
    return num % 10 + recursive_digit_sum(num // 10) if num else 0

#C

def make_equation(*num):
    if len(num) == 1:
        return f'{num[0]}'
    else:
        return f'({make_equation(*num[:-1])}) * x + {num[-1]}'

#D

def answer(func):
    def code(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return code



#E

def result_accumulator(func):
    queue = []

    def wrapper(*args, method='accumulate', **kwargs):
        if method == 'accumulate':
            queue.append(func(*args, **kwargs))
        elif method == 'drop':
            queue.append(func(*args, **kwargs))
            result = queue[:]
            queue.clear()
            return result
    return wrapper