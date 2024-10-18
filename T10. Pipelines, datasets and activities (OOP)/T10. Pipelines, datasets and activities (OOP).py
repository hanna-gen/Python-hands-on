#needs to be enhanced with parameter check and docstrings addition

import pandas as pd
from abc import ABC, abstractmethod
from pprint import pprint
import json 
from genson import SchemaBuilder
import time
import csv
from pprint import pprint

class Dataset(ABC):
    """"""
    @abstractmethod # add to abstract classes
    def preview(self):
        """"""
    @abstractmethod
    def show_schema(self):
        """"""
    @abstractmethod
    def get_data(self):
        """"""   
    @abstractmethod
    def write_data(self):
        """"""
class CSVDataset(Dataset):
    """"""
    def __init__(self, file_path):
        self.file_path = file_path

    def preview(self):
        with open(self.file_path, 'r') as f:
            dataset = csv.reader(f)
            for t in range(0, 3):
                print(next(dataset))

    def show_schema(self):
        df = pd.read_csv(self.file_path)
        return df.dtypes

    def get_data(self):
        df = pd.read_csv(self.file_path)
        return df
    
    def write_data(self, df):
        df.to_csv(path_or_buf=self.file_path, index=False)


class JSONDataset(Dataset):
    """"""
    def __init__(self, file_path):
        self.file_path = file_path

    def preview(self):
        with open(self.file_path, 'r') as f:
            dataset = json.load(f)
            for i in dataset[:3]:
                pprint(i)

    def show_schema(self):
        builder = SchemaBuilder()
        with open(self.file_path, 'r') as f:
            dataset = json.load(f)
            builder.add_object(dataset)
        return builder.to_schema()

    def get_data(self):
        df = pd.read_json(self.file_path)
        return df
    
    def write_data(self, df): 
        df.to_json(path_or_buf=self.file_path)

class Source():
    def __init__(self, dataset: Dataset): 
        self.dataset = dataset

class Sink():
    def __init__(self, dataset: Dataset): 
        self.dataset = dataset

class Activity(ABC):
    """"""
    def start(self):
        """"""
class WaitActivity(Activity):
    """"""
    def __init__(self, time_in_seconds):
        self.time_in_seconds = time_in_seconds

    def start(self): 
        time.sleep(self.time_in_seconds)

class CopyActivity(Activity):
    """"""
    def __init__(self, src, sink):
        self.src = src.dataset
        self.sink = sink.dataset

    def start(self): 
        """start copies the data from the source to the sink"""
        self.sink.write_data(self.src.get_data())


class Pipeline(): 
    """"""
    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)
    
    def execute(self): 
        """iterates through the activities and executes them in order"""
        for a in self.activities:
            a.start()

def main():
    sink = Source(JSONDataset('employment-data.json'))
    src = Sink(CSVDataset('employment-data.csv'))

    copy = CopyActivity(src, sink)
    wait = WaitActivity(5)

    pl = Pipeline()
    pl.add_activity(copy)
    pl.add_activity(wait)
    pl.execute()

if __name__ == '__main__':
    main()