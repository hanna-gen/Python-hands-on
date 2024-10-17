
import importlib
hlp = importlib.import_module('data-helper')

rnd_date = hlp.get_random_date().strftime('%Y/%m/%d')
print(f'This is random date from helper module: {rnd_date}')
print(f'This is random string from helper module: {hlp.get_random_string().upper()}')
print(f'This is random integer from helper module: {hlp.get_random_integer()}')
print(f'This is random double from helper module: {hlp.get_random_double()}')


