import os
import json 
from pprint import pprint

def extract(file_path):
    '''Exports json file data into a list'''
    dataset = list()
    with open(file_path, 'r') as f:
        dataset = json.load(f)
    return dataset

def transform(dataset):
    '''Transforms the dataset by replacint 'name' values with 'NULL' '''
    if type(dataset) == dict and dataset['name']:
        dataset['name'] = 'NULL'
        for i in dataset:
            transform(dataset[i])
    if type(dataset) == list and dataset:
        for i in dataset:
            transform(i)
    return dataset

def load(dataset, file_path):
    '''Loads the transformed dataset to a json file'''
    with open(file_path, 'w') as f:
        json.dump(dataset, f)

def file_path_check(file_path):
    '''Checks if file_path is valid'''
    if not file_path or not isinstance(file_path, str) or not os.path.exists(file_path):
        raise Exception(f'Invalid file path: {file_path}')

def main(src_file_path, trg_file_path):
    file_path_check(src_file_path)   
    file_path_check(trg_file_path)
    print('Extract from json process begins...')
    dataset_raw = extract(src_file_path) 
    print('Extract from json process completed.')
    print('Dataset transformation process begins...')
    dataset_transformed = transform(dataset_raw)
    print('Dataset transformation process completed.')
    print('Loading to json process begins...')
    load(dataset_transformed, trg_file_path)
    print('Loading to json process completed.')

if __name__ == '__main__':
    src_file_path = r'C:\Users\Hanna\Desktop\Python Adastra course\Python hands-on\T3. Anonymize JSON\users_1k.json'
    trg_file_path = r'C:\Users\Hanna\Desktop\Python Adastra course\Python hands-on\T3. Anonymize JSON\users_1k_transformed.json'
    main(src_file_path, trg_file_path)


'''
# additional function to calculate the depth of a json file:
def depth(dataset):
    if type(dataset) == dict and dataset:
        return 1 + max(depth(dataset[i]) for i in dataset)
    if type(dataset) == list and dataset:
        return 1 + max(depth(i) for i in dataset)
    return 0
#print(depth(e))
'''