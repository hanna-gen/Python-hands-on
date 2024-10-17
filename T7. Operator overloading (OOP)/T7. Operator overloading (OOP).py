

class Distance:
    """Distance class that accepts meter, centimeter, and millimeter values and calculates the total distance in millimeters."""
    
    def __init__(self, m, cm, mm):
        self.m = m
        self.cm = cm
        self.mm = mm
    
    @property
    def m(self):
        return self._m
    
    @m.setter
    def m(self, value):
        if not isinstance(value, (int, float)):
            raise Exception(f'Invalid value for \'m\' property: {value}')
        self._m = value

    @property
    def cm(self):
        return self._cm
    
    @cm.setter
    def cm(self, value):
        if not isinstance(value, (int, float)):
            raise Exception(f'Invalid value for \'cm\' property: {value}')
        self._cm = value

    @property
    def mm(self):
        return self._mm
    
    @mm.setter
    def mm(self, value):
        if not isinstance(value, (int, float)):
            raise Exception(f'Invalid value for \'mm\' property: {value}')
        self._mm = value

    @property
    def value(self):
        return self.m*1000 + self.cm*10 + self.mm
    

    def __add__(self, another_object):
        #return self.value + another_object.value # returns int object
        """Returns new Distance object by adding Distance objects"""
        return Distance(self.m + another_object.m, self.cm + another_object.cm, self.mm + another_object.mm) 

    def __sub__(self, another_object):
        """Returns new Distance object by subtracting two Distance objects"""
        return Distance(self.m - another_object.m, self.cm - another_object.cm, self.mm - another_object.mm)
    
    def __iadd__(self, another_object):  
        """Returns new property values to exisiting object by addition assignment operation"""      
        self.m += another_object.m
        self.cm += another_object.cm
        self.mm += another_object.mm
        return self
    
    def __isub__(self, another_object): 
        """Returns new property values to exisiting object by subtraction assignment operation"""
        self.m -= another_object.m
        self.cm -= another_object.cm
        self.mm -= another_object.mm
        return self
    

    def __str__(self):
        return f'Distance({self.m}, {self.cm}, {self.mm}) with calculated value {self.value} mm' 
    
    def __repr__(self): 
        return f'Distance(meters={self.m}, centimeters={self.cm}, millimeters={self.mm})'


def main():
    dist_a = Distance(1, 55, 44) 
    dist_b = Distance(3, 0, 0)
    dist_c = dist_a + dist_b
    print(f'dist_a - standard initialization: {dist_a}')
    print(f'dist_b - standard initialization: {dist_b}')
    print(f'dist_c - initialize from __add__ operator \'dist_a + dist_b\': {dist_c}')

    dist_c += dist_c 
    print(f'dist_c - set new property values to existing object from __iadd__ operator \'dist_c += dist_c\': {dist_c}')

    dist_d = dist_b - dist_a
    print(f'dist_d - initialize from __sub__ operator \'dist_b - dist_a\': {dist_d}')

    dist_d -= dist_b
    print(f'dist_d - set new property values to existing object from __isub__ operator \'dist_d -= dist_b\': {dist_d}')


if __name__ == '__main__':
    main()

