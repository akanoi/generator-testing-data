import sys
import re
import random


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


def generate_phone_number(region, num_digit):
    phone_number_pattern = {
        'BY': '+375 (%d) %d%d%d-%d%d-%d%d',
        'US': '+1 (%d%d%d) %d%d%d%d%d%d%d',
        'RU': '+7 (9%d%d) %d%d%d-%d%d-%d%d',
    }

    digits = tuple(random.randrange(0, 10) for _ in range(num_digit-1))
    if region == 'BY':
        prefix = (17, 25, 29, 33, 44)
        prefix = prefix[random.randrange(0, 5)],  # Convert to tuple
    else:
        prefix = random.randrange(0, 10),

    return phone_number_pattern[region] % (prefix + digits)


region, records_n, errors_n = get_input()

number_digit_in_phone = {
    'BY': 8,
    'US': 10,
    'RU': 9,
}

print(generate_phone_number(region, number_digit_in_phone[region]))