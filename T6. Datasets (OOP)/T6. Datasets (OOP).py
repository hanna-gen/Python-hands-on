from abc import ABC, abstractmethod
import pandas as pd
import pathlib
from datetime import datetime

class Dataset(ABC):
    """Basic representation of a dataset class"""

    @abstractmethod
    def _fetch_data(self):
        """Reads data from file"""

    @abstractmethod
    def _clean_data(self):
        """Drops NA values"""

    @abstractmethod
    def _transform_data(self):
        """At execution point in time, adds current timestamp column to the end of the dataframe"""

    @abstractmethod
    def save_data(self):
        """Saves the transformed data to a target location"""


class CSVDataset(Dataset):
    """CSV Dataset class that accepts a source filepath and a target filepath"""
    def __init__(self, src_filepath: pathlib.Path , target_filepath: pathlib.Path): 
        self.src_filepath = src_filepath 
        self.target_filepath = target_filepath

    def __repr__(self):
        return f"CSVDataset(src_filepath={self.src_filepath}, target_filepath={self.target_filepath})"
    
    def __str__(self):
        return f"CSVDataset({self.src_filepath}, {self.target_filepath})"

    @property
    def src_filepath(self):
        return self._src_filepath
    
    @src_filepath.setter
    def src_filepath(self, value: pathlib.Path):
        if not value or not isinstance(value, pathlib.Path):
            raise Exception("src_filepath must be a valid pathlib.Path object")
        elif value.exists() == False:
            raise Exception(f'No such file or directory: {value}')
        elif value.suffix != '.csv':
            raise Exception("src_filepath must be a.csv file")
        elif value.stat().st_size == 0:
            raise Exception("src_filepath must not be empty")
        self._src_filepath = value
   
    @property
    def target_filepath(self):
        return self._target_filepath
    
    @target_filepath.setter
    def target_filepath(self, value: pathlib.Path):
        if not value or not isinstance(value, pathlib.Path):
            raise Exception("trg_filepath must be a valid pathlib.Path object")
        elif value.parent.exists() == False:
            raise Exception(f'No such parent directory: {value.parent}')
        elif value.suffix != '.csv':
            raise Exception("src_filepath must be a.csv file")
        self._target_filepath = value

    def _fetch_data(self):
        df = pd.read_csv(self.src_filepath) 
        return df

    def _clean_data(self):
        df = self._fetch_data()
        df.dropna(axis=1, how='all', inplace=True) # drop columns where ALL rows are N/A
        return df
    
    def _transform_data(self):
        current_timestamp = datetime.now()
        df = self._clean_data()
        df.insert(loc = len(df.columns), column='Current_timestamp', value=current_timestamp, allow_duplicates=True)
        return df

    def save_data(self):
        df = self._transform_data()
        df.to_csv(path_or_buf=self.target_filepath, index=False)


def main():
    d1 = CSVDataset(pathlib.Path('employment-data.csv'), pathlib.Path('employment-data-transformed.csv'))
    d1.target_filepath = pathlib.Path('employment-data-transformed_new.csv')
    print(d1.__repr__())
    print(d1.__str__())
    d1.save_data()

if __name__ == '__main__':
    main()
