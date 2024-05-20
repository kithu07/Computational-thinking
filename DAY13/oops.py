DIGITS = "123456789"

def min_max(size: int) -> tuple:
    return int(DIGITS[:size]), int(DIGITS[-size:])

class Odometer:                           #class odometer
    def __init__(self, size: int):        #init-->property-->initializes the obj and props
        self._size = size                 #private data var given after _ can be used only within the class  
        self._max, self._min = min_max(size)
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

    
o1 = Odometer(3)                          #o1,o2-->objects
o2 = Odometer(4)
o1.reading = 1239
print(o1.is_ascending())
o1.forward()
print(o1)
o5 = Odometer(5)
o6 = Odometer(5)
print(o5.__eq__(o6))
print(o5 is o6)                         # checks for direct or surface equality