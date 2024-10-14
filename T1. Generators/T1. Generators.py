import os
from random import random, choice
from datetime import datetime, timedelta
from string import ascii_lowercase
import csv

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    '''Generates random date'''
    start = datetime(min_year, 1, 1, 0, 0, 0)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    random_timestamp = start + (end - start) * random()
    return random_timestamp.strftime('%Y-%m-%d 00:00:00')

def gen_boolean():
    '''Generates random boolean value'''
    return choice([True, False])

def gen_word():
    '''Generates random word'''
    return ''.join(choice(ascii_lowercase) for t in range(8))

def gen_data_row(n):
    '''Generator function that yields a row of random data containing a date, a boolean value and a word'''
    for i in range(1, n+1):
        yield i, gen_word(), gen_datetime(), gen_boolean()   

def write_to_csv(file_path: str, nr_of_rows: int):
    '''Uses the generator function and writes the data into a csv file'''

    if not isinstance(file_path, str) or not os.path.exists(file_path):
        raise Exception(f'Invalid file path: {file_path}')
    if not isinstance(nr_of_rows, int) or nr_of_rows <= 0:
        raise Exception(f'Invalid number: {nr_of_rows}. The number must be a positive integer')

    file_name = file_path + r'\random_data.csv'
    with open(file_name, 'w') as file:
        data_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL, lineterminator="\n")
        data_gen = gen_data_row(nr_of_rows)
        for i in range(nr_of_rows):
            data_writer.writerow(next(data_gen))
   

if __name__ == "__main__":
    write_to_csv(
        file_path = r'C:\Users\Hanna\Desktop\Python Adastra course\Python hands-on\T1. Generators'
        ,nr_of_rows = 50
        )


