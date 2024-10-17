from datetime import date, timedelta
from random import random, choice, randint
from string import ascii_lowercase

def get_random_date(min_year=1900, max_year=date.today().year):
    start = date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365) * years
    random_datetime = start + (end - start) * random()
    return random_datetime

def get_random_string(str_len=10):
    return ''.join(choice(ascii_lowercase) for i in range(str_len+1))

def get_random_integer(min_int=0, max_int=1000):
    return randint(min_int, max_int)

def get_random_double(): 
    return random()


if __name__ == '__main__':
    print(get_random_date())
    print(get_random_string())
    print(get_random_integer())
    print(get_random_double())