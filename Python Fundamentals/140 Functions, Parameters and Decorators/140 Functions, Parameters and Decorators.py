import datetime

def log(original_function):
    def new_function(*args, **kwargs):
        with open("log.txt", 'a') as logfile:
            logfile.write(
                "%s: function %s called with positional arguments %s "
                "and keyword arguments %s. \n" %
                (datetime.datetime.now(), original_function.__name__, args, kwargs)
            ) 

        return original_function(*args, **kwargs)
    return new_function

@log 
def my_function(name):
    print("Hello " + name)

my_function('Ivan')
my_function('Hanna')