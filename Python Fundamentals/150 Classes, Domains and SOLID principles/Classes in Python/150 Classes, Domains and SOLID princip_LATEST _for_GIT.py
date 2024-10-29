# 150 Classes, Domains and SOLID principles 
# Class design task 3 
# ETL().source(source_args).sink(sink_args).run()
# {"key": "A123", "value":"15.6", "ts":'2020-10-07 13:28:43.399620+02:00'} 
# NOTE: not a SOLID design principles: it's open to modification b/c of many hardcoded values - in real life it needs to be modified to be more generic and flexible

import json
import websocket
import psycopg2
import pathlib
from pprint import pprint
import args

class ETL: 

    def __init__(self):   
        # value assigned in self.source() - can be 'f' for file, or 's' for simulation:
        self.source_type = ''

        # value assigned in self.source() - for 'f' source only:
        self.file_path = pathlib.Path

        # value incremented in self.source() - max count of messages per run - for 's' source only:
        self.msg_cnt = 0

        # value assigned in self.sink() - can be 'p' for print to Console, or 'db' for PostgreSQL
        self.sink_type = ''

        # value assigned in self.sink() - for 'db' sink_type only:
        self.sql_create=""""""
        self.sql_insert=""""""
        
        # # value assigned in self.sink() - for 'db' sink_type and 's' source_type only:
        self.sql_max_pk="""""" 

        self.data = [] 


    def _from_json(self):
        with open(self.file_path) as f: 
            raw_data = f.read() #interpreted as string
            self.data = json.loads(raw_data.replace("'", '"')) #interpreted as array/list of dict's

    def _from_simulation(self, max_cnt):   
        def on_message(ws, message):
            cnt = 0
            while cnt <= max_cnt:        
                # init dict for every message:
                msg_dict = json.loads(message)
                self.data.append(msg_dict) 
                cnt += 1
            ws.close()        
        
        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")

        def on_open(ws):
            ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=ci89d39r01qnrgm33an0ci89d39r01qnrgm33ang",
                                    on_message = on_message,
                                    on_error = on_error,
                                    on_close = on_close)
        ws.on_open = on_open
        ws.run_forever() 

    def _to_PostgreSQL(self):
        conn = psycopg2.connect("dbname=postgres user=postgres password=********")
        # Open a cursor to perform database operations
        cur = conn.cursor()
        # Execute a query
        cur.execute(self.sql_create)

        if self.source_type == 's':
            cur.execute(self.sql_max_pk)
            pk=cur.fetchone()[0]

        for d in self.data:  
            val_list=[]  

            if self.source_type == 'f':
                val_list = [d['key'], d['value'], d['ts']]

            elif self.source_type == 's':
                if pk == None:
                    pk = 0
                elif pk != None:
                    pk=int(pk)
                pk += 1
                val_list = [pk, str(d)]
            
            cur.execute(self.sql_insert, val_list)

        #Retrieve query results: var = cur.fetchall()
        conn.commit()

    def _to_console(self):
        pprint('Print to console: {}'.format(str(self.data)))


    def source(self, source_type, file_path=''): #source_type can be 'f' for file, or 's' for simulation; optional file_path for 'f' source, max_cnt of messages for 's' source
        if source_type not in ('f','s'):
            raise Exception('source_type can be either\'f\' for file, or \'s\' for simulation')
        self.source_type = source_type

        if self.source_type == 'f': 
            if not file_path or not isinstance(file_path, pathlib.Path):
                raise Exception("file_path must be a valid pathlib.Path object")
            elif file_path.exists() == False:
                raise Exception(f'No such file or directory: {file_path}')
            elif file_path.suffix != '.json':
                raise Exception("file_path must be a json file")
            elif file_path.stat().st_size == 0:
                raise Exception("file_path must not be empty")
            
            self.file_path = file_path
            self._from_json()     

        elif self.source_type == 's':
            max_cnt = input('Enter the number of messages to be generated: ')
            try:
                max_cnt = int(max_cnt)
            except:
                raise Exception('Invalid number for messages to be generated')
            self.msg_cnt += max_cnt
            self._from_simulation(max_cnt)          
 
        return self
     
    
    def sink(self, sink_type, sql_create="""""", sql_insert="""""", sql_max_pk=""""""): #sink_type can be 'p' for print to Console, or 'db' for PostgreSQL
        if sink_type not in ('p', 'db'):
            raise Exception('sink_type can be \'p\' for print to Console, or \'db\' for PostgreSQL')
        self.sink_type = sink_type

        if self.sink_type == 'db':
            # more advanced sql query check may be applied
            if len(sql_create) == 0:
                raise Exception('sql_create cannot be empty')
            if len(sql_insert) == 0:
                raise Exception('sql_insert cannot be empty') 
            self.sql_create = sql_create
            self.sql_insert = sql_insert

            if self.source_type == 's':
                if len(sql_max_pk) == 0:
                    raise Exception('sql_max_pk cannot be empty')  
                self.sql_max_pk = sql_max_pk
            self._to_PostgreSQL()

        # Data sink is Console: the consumed messages are printed to stdout
        elif self.sink_type == 'p':
            self._to_console()      

        return self
    

    def run(self):
        if self.source_type == 'f':
            print('Execution completed')

        elif self.source_type == 's':
            command = input('Please type \'end\' to stop, or type \'go\' to continue: ')
            if command != 'end':
                if self.sink_type == 'p':
                    self.source(source_type = self.source_type).sink(sink_type = self.sink_type).run()    
                elif self.sink_type == 'db':
                    self.source(source_type = self.source_type).sink(sink_type = self.sink_type, sql_create = self.sql_create, sql_insert = self.sql_insert, sql_max_pk = self.sql_max_pk).run() 
            else:
                print('Execution completed')    



if __name__ == '__main__':

    data1=ETL()

    data1.source(
    source_type = 's'
    #source_type = 'f'
    #,file_path = pathlib.Path(args.file_path)
    ).sink(
    sink_type = 'p'
    #sink_type='db'
    #,sql_create = args.sql_create_tbl_for_file_src
    #,sql_insert = args.sql_insert_tbl_for_file_src 
    #,sql_create = args.sql_create_tbl_for_simul_src
    #,sql_insert = args.sql_insert_tbl_for_simul_src
    #,sql_max_pk = args.sql_max_pk_for_simul_src
    ).run()



