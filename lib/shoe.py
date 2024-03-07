#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self._condition = 'New'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
        
    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, value):
        self._condition = value
        
    def repair(self):
        print ("The shoe has been repaired.")
        self._condition = 'New'

    def cobble(self):  
        print ("Your shoe is as good as new!")
        