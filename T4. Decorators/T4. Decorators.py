
def split_decorator(original_function):
    '''Decorator that accepts a string output from the original function and splits it into words with a space separator'''
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs).split()
        print(f'Result of split decorator is: {result}')
        return result
    return wrapper_function

def upper_decorator(original_function):
    '''Decorator that accepts a string output from the original function and makes all words uppercase'''
    def wrapper_function(*args, **kwargs):
        result = [w.upper() for w in original_function(*args, **kwargs)]
        print(f'Result of uppercase decorator is: {result}')
        return result
    return wrapper_function

def filter_decorator(original_function):
    '''Decorator that accepts a string output from the original function and removes all words with < 4 characters length'''
    def wrapper_function(*args, **kwargs):
        result = list(filter(lambda x: x if len(x) >= 4 else None, original_function(*args, **kwargs)))
        print(f'Result of filter decorator is: {result}')
        return result
    return wrapper_function

# additional excercise - timer decorator
import time
def timer_decorator(original_function):
    '''Decorator that calculates the execution time of the original function'''
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f'Execution time of original function {original_function.__name__} is {delta_time}')
        return result
    return wrapper_function


# order of execution - bottom >> top
# mind the data type each one decorator returns
@filter_decorator # returns list
@upper_decorator # returns list
@split_decorator # returns list
@timer_decorator
def get_data(x):
    print(f'Result of original function is: {x}')
    return x


if __name__ == '__main__':
    get_data('This is An exAmPlE StRinG')


