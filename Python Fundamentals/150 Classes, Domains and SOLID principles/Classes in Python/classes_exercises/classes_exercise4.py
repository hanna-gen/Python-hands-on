# https://python-textbok.readthedocs.io/en/1.0/Classes.html


class Numbers:
    MULTIPLIER=2

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def add(self):
        res=self.x+self.y
        return res
    
    @classmethod
    def multiply(cls, a):
        res=cls.MULTIPLIER*a
        return res
    
    @staticmethod
    def subtract(b, c):
        res=b-c
        return res
    
    @property
    def value(self):
        return (self.x, self.y) 
    
    @value.setter
    def value(self, new_val_tpl):
        self.x, self.y = new_val_tpl
    
    @value.deleter 
    def value(self):
        del self.x 
        del self.y
  
nr=Numbers(1,3)
print(nr.add())
print(nr.multiply(4))
print(nr.subtract(8,5))
print(nr.value)
print('after change >>>>>>>>>>>>>>>>')
nr.value = (8,8)
print(nr.add())
print(nr.value)
print(dir(nr))
print(nr.__dict__)

