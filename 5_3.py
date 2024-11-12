5_3

# A

try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except SystemError:
    print('SystemError')
except Exception as e:
    print('Unexpected error: {e}')
else:
    print('No Exceptions')

# B

a = 'str' 
b = (3, 5)

func(a, b)

# C

class MyClass:

    def __repr__(self) -> str:
        raise Exception


a = MyClass()
func(a)

# D

def only_positive_even_sum(*args):
    for item in args:
        if not isinstance(item, int):
            raise TypeError
    for item in args:
        if item <= 0 or item % 2 != 0:
            raise ValueError
    return sum(args)

# E

def check_queue_iterated(*queues):
    for queue in queues:
        try:
            iter(queue)
        except TypeError:
            raise StopIteration


def check_queue_consistence(*queues):
    queue = []
    for queue_in_queues in queues:
        queue.extend(list(queue_in_queues))
    if not all(type(member) is type(queue[0]) for member in queue):
        raise TypeError


def check_queue_sorted(*queues):
    for queue in queues:
        if list(queue) != sorted(queue):
            raise ValueError
    return True


def merge(queue_1, queue_2):
    check_queue_iterated(queue_1, queue_2)
    check_queue_consistence(queue_1, queue_2)
    check_queue_sorted(queue_1, queue_2)
    queue_1n = list(queue_1)
    queue_2n = list(queue_2)
    sequence = []

    while queue_1n and queue_2n:
        if queue_1n[0] > queue_2n[0]:
            sequence.append(queue_2n.pop(0))
        else:
            sequence.append(queue_1n.pop(0))
    sequence.extend(queue_1n + queue_2n)
    return sequence
