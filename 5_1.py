# A
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

# B

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)
    
# C
class RedButton:
    def __init__(self) -> None:
        self.counter = 0

    def click(self):
        self.counter += 1
        print('Тревога!')

    def count(self):
        return self.counter

# D

class Programmer:
    __wage = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }

    __ranks = list(dict(sorted(__wage.items(), key=lambda item: item[1])).keys())  # noqa

    def __init__(self, name, position) -> None:
        self.__name = name
        self.__position = position
        self.__bonus = 0
        self.__work_time = 0
        self.__salary = 0

    def work(self, time):
        self.__work_time += time
        self.__salary += (self.__wage[self.__position] + self.__bonus) * time

    def info(self):
        return f'{self.__name} {self.__work_time}ч. {self.__salary}тгр.'

    def rise(self):
        if self.__position != self.__ranks[-1]:
            index = self.__ranks.index(self.__position)
            self.__position = self.__ranks[index + 1]
        else:
            self.__bonus += 1



# E

class Rectangle:
    def __init__(self, *coords):
        self.coords = coords
        self.width = abs(self.coords[0][0] - self.coords[1][0])
        self.height = abs(self.coords[0][1] - self.coords[1][1])

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)