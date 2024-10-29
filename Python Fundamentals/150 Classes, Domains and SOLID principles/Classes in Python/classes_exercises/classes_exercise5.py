# https://python-textbok.readthedocs.io/en/1.0/Classes.html

import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age 

    def print_custom_attr(self):
        for k, v in self.__dict__.items():
            print('%s: %s' % (k, v))

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())

#print(dir(person))
#print(dir(Person))
#print(person.__str__())
#print(str(person))
#print(type(person))
#print(type(Person))
#print(person.__dict__)
#person.print_custom_attr()
print(person)