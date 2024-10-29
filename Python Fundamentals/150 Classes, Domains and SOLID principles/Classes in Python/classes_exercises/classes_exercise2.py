# https://python-textbok.readthedocs.io/en/1.0/Classes.html

#n = 1 #integer is type/class, n is object/instance, 1 is attribute; function is method

#Rewrite the Person class so that a person’s age is calculated for the first time when a new person instance is created, and recalculated (when it is requested) 
#if the day has changed since the last time that it was calculated.

import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

        # This isn't strictly necessary, but it clearly introduces these attributes
        self._age = None
        self._age_last_calc_day = None

        self._recalculate_age()

    def _recalculate_age(self):
        today = datetime.date.today()    
        age = today.year - self.birthdate.year 
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        
        self._age = age 
        self._age_last_calc_day = today

    def age(self):
        if (datetime.date.today() > self._age_last_calc_day):
            self._recalculate_age()
        return self._age
    
person = Person('H', 'M', datetime.date(1986,4,7), 'lviv', 111, 'h@m')
print(person.age())
