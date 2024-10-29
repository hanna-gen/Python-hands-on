# https://python-textbok.readthedocs.io/en/1.0/Classes.html

class Generic():
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            #self.k = v #WRONG!!!
            setattr(self,k,v)

    def __str__(self):
        attr=['%s=%s' % (k,v) for k,v in self.__dict__.items()]
        classname=self.__class__.__name__
        return '%s: %s' % (classname, ' '.join(attr))

rnd1=Generic(name='HM', age=6)
print(rnd1)