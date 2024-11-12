# A

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


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args


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


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)

    def __str__(self) -> str:
        string = f'({self.x}, {self.y})'
        return string

    def __repr__(self) -> str:
        string = f'PatchedPoint({self.x}, {self.y})'
        return string

# C

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


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                super().__init__(0, 0)
            case 1:
                super().__init__(*args[0])
            case 2:
                super().__init__(*args)

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self

    def __str__(self) -> str:
        string = f'({self.x}, {self.y})'
        return string

    def __repr__(self) -> str:
        string = f'PatchedPoint({self.x}, {self.y})'
        return string

# D

class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __reduction(self):
        gcd = self.__gcd(self.__num, self.__den)
        self.__num = self.__num // gcd
        self.__den = self.__den // gcd
        return self

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction({self.__num}, {self.__den})"

    def numerator(self, *args):
        if len(args):
            self.__num = args[0]
            self.__reduction()
        return self.__num

    def denominator(self, *args):
        if len(args):
            self.__den = args[0]
            self.__reduction()
        return self.__den


# E

class Fraction():
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> 'Fraction':
        __gcd = self.__gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)