import sys
import re


ERR_NUMBER_PARAMETERS= 'A small number of input parameters!'
ERR_REGION_NAME = 'Invalid region name! (US, RU, BY)'
ERR_NUMBER_RECORDS = 'Invalid number records! (1..10.000.000)'
ERR_NUMBER_ERRORS = 'Invalid number errors! (>= 0)'


def get_input():
    if len(sys.argv) != 4:  
        raise Exception(ERR_NUMBER_PARAMETERS)

    if re.match(r"BY|RU|US", sys.argv[1]) == None:
        raise Exception(ERR_REGION_NAME)

    if (int(sys.argv[2]) < 1) or (int(sys.argv[2]) > 10000000):
        raise Exception(ERR_NUMBER_RECORDS)
    
    if int(sys.argv[3]) < 0:
        raise Exception(ERR_NUMBER_ERRORS)

    return sys.argv[1], sys.argv[2], sys.argv[3]


region, records_n, errors_n = get_input()
