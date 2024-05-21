DIGITS = "123456789"

def min_max(size: int) -> tuple:
    return int(DIGITS[:size]), int(DIGITS[-size:])

class Odometer:                           #class odometer
    def __init__(self, size: int):        #init-->property-->initializes the obj and props
        self._size = size                 #private data var given after _ can be used only within the class  
        self._min, self._max = min_max(size)
        self.reading = self._min          #reading-->property

    def __str__(self) -> str:
        return f'<{self.reading} >'
    
    def __eq__(self, other):
        return self.reading == other.reading 
    
    def __repr__(self) -> str:
        size = len(str(self.reading))
        return f'Size: {size}, Reading: {self.reading}'
    
    def is_ascending(self) -> bool:
        return all(a<b for a, b in zip(str(self.reading), str(self.reading)[1:]))
    
    def forward(self):
        if self.reading == self._max:
            self.reading = self._min
        else:
            self.reading += 1
            while not self.is_ascending():
                self.reading += 1

    def backward(self):
        if self.reading == self._min:
            self.reading = self._max
        else:
            self.reading -= 1
            while not self.is_ascending():
                self.reading -= 1

    def n_steps_forward(self, n: int):
        for step in range(n):
            self.forward()

    def n_steps_backward(self, n: int):
        for step in range(n):
            self.backward()

    def no_of_steps(self, reading2):
        steps = 0
        while self.reading != reading2:
            self.forward()
            steps += 1           
        return steps    
    
o1 = Odometer(3)
print(o1)
o1.forward()
print(o1)
o1.backward()
print(o1)
o1.n_steps_forward(3)
print(o1)
o1.n_steps_backward(3)
print(o1)
print(o1.no_of_steps(157))
