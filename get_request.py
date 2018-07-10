import argparse
import requests
import datetime
import sys
from time import time, sleep

END_POINT = ''

def arg_parser():
    global END_POINT
    parser = argparse.ArgumentParser()
    parser.add_argument("ENDPOINT_URL",
                        type=str,
                        help="endpoint url")
    args = vars(parser.parse_args())
    END_POINT = args['ENDPOINT_URL']
        
def main():
    counter = 0
    request_id = 0
    start = time()
    started = str(datetime.datetime.now())
    while True: #time() - start <= 1:
        r = requests.get(END_POINT)
        request_id += 1
        counter += 1
        if time()-start >= 1:
            sys.stdout.write("[Request#%d]\t %d requests/second\n" %(request_id, counter) )
            counter = 0
            start = time()
            
if __name__ == '__main__':
    arg_parser()
    main()
