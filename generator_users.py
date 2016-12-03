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

    return sys.argv[1], int(sys.argv[2]), int(sys.argv[3])


def generate_phone_number(region):
    phone_number_pattern = {
        'BY': '+375-%d-%d%d%d-%d%d-%d%d',
        'US': '+1-%d%d%d-%d%d%d-%d%d%d%d',
        'RU': '+7-9%d%d-%d%d%d-%d%d-%d%d',
    }

    number_digit_in_phone = {
        'BY': 8,
        'US': 10,
        'RU': 9,
    }

    num_digit = number_digit_in_phone[region]

    digits = tuple(random.randrange(0, 10) for _ in range(num_digit-1))
    if region == 'BY':
        prefix = (17, 25, 29, 33, 44)
        prefix = prefix[random.randrange(0, 5)],  # Convert to tuple
    else:
        prefix = random.randrange(0, 10),

    return phone_number_pattern[region] % (prefix + digits)


def get_record(name, surname, addres, region, phone, index, middlename=''):
    region_name = {
        'BY': 'Беларусь',
        'RU': 'Россия',
        'US': 'USA',
    }

    return '{0} {1} {2}; {3}, {4}, {5}; {6}' \
            .format(name, middlename, surname, addres, index, region_name[region], phone)


def set_error(record):
    chars = 'qwertyuiop[]asdfghjkl;zxcvbnm,.1234567890йцукенгшщзхфывапролджэячсмитьбю'


    def swap(item, index):
        return item[:index] + item[index+1] + item[index] + item[index+1:]

    def delete(item, index):
        return item[:index] + item[index+1:]

    def double(item, index):
        return item[:index+1] + item[index] + item[index+1:]

    def insert(item, index):
        return item[:index+1] + chars[random.randrange(0, len(chars))] + item[index:]

    def replace(item, index):
        return item[:index] + chars[random.randrange(0, len(chars))] + item[index+1:]


    random_item = random.randrange(0, 7)
    item = record[random_item]
    index = random.randrange(1, len(item-1))

    fun_number = random.randrange(0, 5)
    if fun_number == 0:
        record[random_item] = swap(item, index)
    if fun_number == 1:
        record[random_item] = delete(item, index)
    if fun_number == 2:
        record[random_item] = double(item, index)
    if fun_number == 3:
        record[random_item] = insert(item, index)


region, records_n, errors_n = get_input()

for _ in range(records_n):
    phone = generate_phone_number(region)
    print(get_record('Алег', 'Канойка', 'Минск ул.Судмалиса 26', region, phone, '222202', 'Игаравич'))
