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
    prevCounter = 0
    start = time()
    started = str(datetime.datetime.now())
    while True: #time() - start <= 1:
        r = requests.get(END_POINT)
        counter += 1
        if (counter-prevCounter) >= 100:
            sys.stdout.write("Requests#: [%d] \n" % counter )
            prevCounter = counter
            
if __name__ == '__main__':
    arg_parser()
    main()
