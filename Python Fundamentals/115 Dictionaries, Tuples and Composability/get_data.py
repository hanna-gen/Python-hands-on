
import json
import websocket
from datetime import datetime, timedelta

#list of items used to calculate vvwap:
pricePerVol=[]
vol = []

#dict that stores all calculated data and vwap value, it is also written to a file
vwap_dict = {}

#time control pointer, initiated as process start time:
start_time=datetime.now().replace(microsecond=0) # 2024-10-23 16:24:17

#note for late arriving data >> to print out and add to vvwap_dict.txt
update_note = 'UPDATED for late arriving data >> '

#format unix_timestamp e.g. '1687202120662' to '2023-11-09 10:58:08'
def format_tm(unix_timestamp):
    output_format = '%Y-%m-%d %H:%M:%S'
    time_formatted = datetime.strptime(datetime.fromtimestamp(unix_timestamp/1000.0).strftime(output_format), output_format)
    return time_formatted

#calculate end of processed minute period
def calc_end_time(start_tm):
    end_tm = start_tm + timedelta(seconds=59-start_tm.second)
    return end_tm

#calculate the volume-weighted average price (vvwap), using sum of items in lists pricePerVol, vol >> called in insert_vwap() and update_vwap():
def calculate_vwap(pricePerVolSum, volSum):
    result = pricePerVolSum/volSum 
    return result

#insert new record into vvwap_dict for each one minute period (e.g. 10:00-10:01, 10:01-10:02, etc.) 
def insert_vwap(st_tm, pv, v): 
    start_time = st_tm
    end_time = calc_end_time(st_tm)
    vwap = calculate_vwap(sum(pv), sum(v))
    vwap_dict[ 
        (start_time, end_time)
        ] = {
                'pricePerVol': pv,
                'vol': v,
                'pricePerVolSum': sum(pv),
                'volSum': sum(v),
                'vwap': vwap
            } 
    print_vwap(start_time, end_time, vwap)
    write_to_file(f'{start_time} - {end_time}: {vwap_dict[(start_time, end_time)]}')

#update vvwap_dict only if there is existing data for whole 1-minute past cycle; else: drop data - no need in partial data
def update_vwap(tm, newPricePerVol, newVol): 
    for k, v in vwap_dict.items():
        if tm >= k[0] and tm <= k[1]:
            v['pricePerVol'].append(newPricePerVol)
            v['vol'].append(newVol)
            v['pricePerVolSum'] += newPricePerVol
            v['volSum'] += newVol
            new_vwap = calculate_vwap(v['pricePerVolSum'], v['volSum'])
            v['vwap'] = new_vwap

            past_start_time = k[0]
            past_end_time = k[1]
            print_vwap(past_start_time, past_end_time, new_vwap, late_data=True)
            write_to_file(f'{k[0]} - {k[1]}: {v}')

def print_vwap(start_time, end_time, vwap, late_data=False):
    msg = 'time: {} - {}, vwap: {}'.format(start_time, end_time, vwap)
    if late_data == True:
        msg = update_note + msg
    print(msg)

def write_to_file(vvwap_dict):
    border='###############################################################################'
    with open(r".\vwap_dict.txt", "a") as f: 
        f.write(str(vvwap_dict)+'\n'+border+'\n')

#function to coordinate population of vvwap_dict:
def run_vwap(d):
    global pricePerVol
    global vol
    global start_time
    #iterate through the message dict:
    for i in d['data']:
        #if current time in message dict is betwween time control pointer and calculated end of processed minute period:
        if format_tm(i['t']) >= start_time and format_tm(i['t']) <= calc_end_time(start_time):
            #pass to append vol, pricePerVol
            pass

        #if current time in message dict is greater than calculated end of processed minute period:
        elif format_tm(i['t']) > calc_end_time(start_time):
            #insert into vvwap_dict
            insert_vwap(start_time, pricePerVol, vol) 
            #change value of time control pointer to current time in message dict:
            start_time = format_tm(i['t']) 
            #empty below lists:
            pricePerVol=[]
            vol = []
            #pass to append vol, pricePerVol
            pass

        #for late arriving data: if current time in message dict is less than time control pointer:
        elif format_tm(i['t']) < start_time:
            #update vvwap_dict if previous one minute period is already existing in the same:
            update_vwap(format_tm(i['t']), i['p']*i['v'], i['v'])

        pricePerVol.append(i['p']*i['v'])
        vol.append(i['v'])

# main set of functions to trigger coordination of vvwap_dict population on every message
def on_message(ws, message):
    #init dict for every message: see sample data structure commented OUT at the bottom of the script
    msg_dict = json.loads(message)

    #output in the console all relevant trades in the required format: 
    for i in msg_dict['data']:
        tm = i['t'] / 1000.0
        new_tm = datetime.fromtimestamp(tm).strftime('%Y-%m-%d %H:%M:%S') 
        print('{} price:{} volume:{}'.format(new_tm,i['p'],i['v']))

    #for each one minute period (e.g. 10:00-10:01, 10:01-10:02, etc.) calculate the volume-weighted average price (vvwap) of trades made during this minute:
    run_vwap(msg_dict)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=ci89d39r01qnrgm33an0ci89d39r01qnrgm33ang",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()


'''
SAMPLE MESSAGE STRUCTURE >>

msg_dict = {'data': 
[
{'c': None, 'p': 26626, 's': 'BINANCE:BTCUSDT', 't': 1687202120662, 'v': 0.04755}     #Monday, June 19, 2023 10:15:20.662 PM GMT+03:00 DST
,{'c': None, 'p': 26626.01, 's': 'BINANCE:BTCUSDT', 't': 1687202120797, 'v': 0.01198} #Monday, June 19, 2023 10:15:20.797 PM GMT+03:00 DST
,{'c': None, 'p': 26626.01, 's': 'BINANCE:BTCUSDT', 't': 1687246559000, 'v': 0.01198} #Tuesday, June 20, 2023 10:35:59 AM GMT+03:00 DST
,{'c': None, 'p': 26626.01, 's': 'BINANCE:BTCUSDT', 't': 1687250159000, 'v': 0.01198} #Tuesday, June 20, 2023 11:35:59 AM GMT+03:00 DST
,{'c': None, 'p': 26626.01, 's': 'BINANCE:BTCUSDT', 't': 1687202125000, 'v': 0.01198} #late data - Monday, June 19, 2023 10:15:25 PM GMT+03:00 DST
], 
'type': 'trade'}
'''
