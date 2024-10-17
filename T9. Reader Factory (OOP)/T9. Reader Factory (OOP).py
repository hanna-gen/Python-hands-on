
from abc import ABC, abstractmethod
import args
import pandas as pd

class Reader(ABC):
    """Reads data from source and returns pandas dataframe"""
    @abstractmethod
    def read(self):
        """Performs the reading operation"""

class CSVReader(Reader):
    """Reads data from csv and returns pandas dataframe"""
    def __init__(self, src_filepath):
        self.src_filepath = src_filepath

    def read(self):
        try: 
            df = pd.read_csv(self.src_filepath)
            return df
        except FileNotFoundError:
            return f'No such file or directory: {self.src_filepath}'

class JSONReader(Reader):
    """Reads data from json and returns pandas dataframe"""
    def __init__(self, src_filepath):
        self.src_filepath = src_filepath

    def read(self):
            try:
                df = pd.read_json(self.src_filepath)
                return df
            except ValueError:
                return f'Expected object or value: {self.src_filepath}'
       

class DatabaseReader(Reader): 
    """Reads data from database and returns pandas dataframe"""
    def __init__(self, dbname, user, password, schema_name, table_name): # may also add host, port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.schema_name = schema_name
        self.table_name = table_name
    
    def read(self):
        import psycopg2
        with psycopg2.connect(f"dbname={self.dbname} user={self.user} password={self.password}") as conn:
            sql = f"select * from {self.schema_name}.{self.table_name}"
            df = pd.read_sql(sql=sql, con=conn)
        return df


class ReaderFactory():
    """Returns desired reader object based on reader_type argument: 'csv', 'json', 'db'."""
    @staticmethod
    def get_reader(reader_type):
        factories = {
            'csv': CSVReader(args.csv_path),
            'json': JSONReader(args.json_path),
            'db': DatabaseReader(args.dbname, args.user, args.password, args.schema_name, args.table_name)
        }
        if reader_type in factories:
            return factories[reader_type]    
        print('Unknown source: {source}')


def main():
    fact = ReaderFactory().get_reader('json')
    print(fact.read())


if __name__ == '__main__':
    main()





