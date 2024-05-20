DIGITS = '123456789'

def min_max(size: int) -> tuple:
    return int(DIGITS[:size]), int(DIGITS[-size:])

class Odometer:
    def __init__(self, size: int) -> None:
        self._size = size
        self._min, self._max = min_max(size)
        self._reading = self._min

    def reading(self) -> int:
        return self._reading

    def __str__(self) -> str:
        return f'<{self._reading}>'
    
    def __repr__(self) -> str:
        size = len(str(self._reading))
        return f'Size: {size}, Reading: {self._reading}'
    
    def __eq__(self, other) -> bool:
        if self._size != other._size:
            raise ValueError(f"Incomparable Odometers: sizes {self._size}, {other._size}")
        return self._reading == other._reading
    
    def __lt__(self, other) -> bool:
        if self._size != other._size:
            raise ValueError("Odometers of different sizes are incomparable")
        return self._reading < other._reading
    
    @classmethod
    def is_ascending(cls, reading) -> bool:
        return all(a < b for a, b in zip(str(reading), str(reading)[1:]))

    def forward(self, step:int=1) -> None:
        for _ in range(step):
            if self._reading == self._max:
                self._reading = self._min
            else:
                self._reading += 1
                while not Odometer.is_ascending(self._reading):
                    self._reading += 1


o1 = Odometer(3)
o2 = Odometer(4)
print(o1)
o1._reading = 1239
print(Odometer.is_ascending(o1.reading()))
Odometer.forward(o1)
o1.forward()
print(o1)

o5 = Odometer(5)
o6 = Odometer(5)

o6.forward()

print(o5 == o6)
print(o5.__eq__(o6))

print(o5 is o6)

o6.forward = lambda x: "hello world"

print(o5)

o5.forward()

print(o5)
