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
        copy = Odometer(self._size)
        copy.reading = self.reading
        if copy.reading == self._max:
            copy.reading = self._min
        else:
            copy.reading += 1
            while not copy.is_ascending():
                copy.reading += 1
        return copy
    

    def backward(self):
        temp_obj = Odometer(self._size)
        temp_obj.reading = self.reading
        if temp_obj.reading == self._min:
            temp_obj.reading = self._max
        else:
            temp_obj.reading -= 1
            while not temp_obj.is_ascending():
                temp_obj.reading -= 1
        return temp_obj

    def n_steps_forward(self, n: int):
        dup = Odometer(self._size)
        dup.reading = self.reading
        for step in range(n):
            dup = dup.forward()
        return dup

    def n_steps_backward(self, n: int):
        dup = Odometer(self._size)
        dup.reading = self.reading
        for step in range(n):
            dup = dup.backward()
        return dup
    
    def distance(self, reading2):
        steps = 0
        dup = Odometer(self._size)
        dup.reading = self.reading
        while dup.reading != reading2:
            dup = dup.forward()
            steps += 1         
        return steps    
    
o1 = Odometer(3)
print(o1)
print(o1.forward())
print(o1.backward())
print(o1.n_steps_forward(3))
print(o1.n_steps_backward(3))
print(o1)
print(o1.distance(157))
print(o1)
