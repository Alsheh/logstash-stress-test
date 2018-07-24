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
    while True: 
        r = requests.get(END_POINT + '/test-%d' % counter)
        counter += 1
        if counter % 100 == 0:
            print "Reqeust#", counter

if __name__ == '__main__':
    arg_parser()
    main()
