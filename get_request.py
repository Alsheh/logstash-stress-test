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
    i = 0
    start = time()
    started = str(datetime.datetime.now())
    while True: #time() - start <= 1:
        r = requests.get(END_POINT)
        i += 1
    sys.stdout.write("Started: [%s] Exited: [%s] Duration: [%s] Requests#: [%d] \n" % (
        started,
        str(datetime.datetime.now()),
        time() - start,
        i
    ))

if __name__ == '__main__':
    arg_parser()
    main()
