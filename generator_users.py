import sys
import re
import random
import csv
from math import ceil, modf


ERR_NUMBER_PARAMETERS= 'A small number of input parameters!'
ERR_REGION_NAME = 'Invalid region name! (US, RU, BY)'
ERR_NUMBER_RECORDS = 'Invalid number records! (1..10.000.000)'
ERR_NUMBER_ERRORS = 'Invalid number errors! (>= 0)'


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

    digits = tuple(random.randint(0, 10) for _ in range(num_digit-1))
    if region == 'BY':
        prefix = random.choice([17, 25, 29, 33, 44]), # Convert to tuple
    else:
        prefix = random.randint(0, 10),

    return phone_number_pattern[region] % (prefix + digits)


def generate_human(region):
    file_name = open("data/%s_name.txt" % region.lower(), "r")
    file_surname = open("data/%s_surname.txt" % region.lower(), "r")
    
    name = random.choice(list(file_name)).strip()
    surname = random.choice(list(file_surname)).strip()

    file_name.close()
    file_surname.close()
    
    return name, surname


def generate_addres(region):
    file_streets = open("data/%s_street.txt" % region.lower(), "r")
    street = random.choice(list(file_streets)).strip()
    file_streets.close()

    file_citys = open("data/%s_city.txt" % region.lower(), "r")
    random_city = random.choice(list(file_citys)).split()
    file_citys.close()

    city = random_city[0]
    index = random_city[1][:-2]
    index += str(random.randint(0, 9)) + str(random.randint(0, 9))

    house = random.randint(1, 25)
    appartement = random.randint(1, 50)

    return "%s, %s %s %s" % (city, street, house, appartement), index


def record(name, surname, addres, region, phone, index):
    region_name = {
        'BY': 'Беларусь',
        'RU': 'Россия',
        'US': 'USA',
    }

    return '{0} {1}; {2}, {3}, {4}; {5};' \
            .format(name, surname, addres, index, region_name[region], phone)


def set_error(item):
    chars = 'qwertyuiop[]asdfghjkl;zxcvbnm,.1234567890йцукенгшщзхфывапролджэячсмитьбю'


    def swap(index):
        return item[:index] + item[index+1] + item[index] + item[index+1:]

    def delete(index):
        return item[:index] + item[index+1:]

    def double(index):
        return item[:index+1] + item[index] + item[index+1:]

    def insert(index):
        return item[:index+1] + random.choice(chars) + item[index:]

    def replace(index):
        return item[:index] + random.choice(chars) + item[index+1:]


    index = random.randint(0, len(item)-2)
    fun_number = random.randint(0, 4)
    if fun_number == 0:
        return swap(index)
    if fun_number == 1:
        return delete(index)
    if fun_number == 2:
        return double(index)
    if fun_number == 3:
        return insert(index)
    if fun_number == 4:
        return replace(index)


def get_input():
    if len(sys.argv) != 4:  
        raise Exception(ERR_NUMBER_PARAMETERS)

    if re.match(r"BY|RU|US", sys.argv[1]) == None:
        raise Exception(ERR_REGION_NAME)

    if (int(sys.argv[2]) < 1) or (int(sys.argv[2]) > 10000000):
        raise Exception(ERR_NUMBER_RECORDS)
    
    if float(sys.argv[3]) < 0:
        raise Exception(ERR_NUMBER_ERRORS)

    return sys.argv[1], int(sys.argv[2]), float(sys.argv[3])


def get_count_errors(err, rec):
    if err == 0:
        return 0, 0

    if not err.is_integer() and (err < 1):
        return ceil(rec * err), 0
    elif rec > err:
        return 0, ceil(rec / err)
    else:
        return modf(err / rec)


region, records_n, errors_n = get_input()
error_per_n, error_per_record = get_count_errors(errors_n, records_n)

buf_record = []

count_err = 0
for i in range(records_n):
    phone = generate_phone_number(region)
    name, surname = generate_human(region)
    addres, index = generate_addres(region)
    tmp_record = [name, surname, addres, phone, index]

    for _ in range(ceil(error_per_record)):
        if count_err != errors_n:
            item = random.randint(0, 4)
            tmp_record[item] = set_error(tmp_record[item])
            count_err += 1

    if (count_err != errors_n) and random.randint(0, 2):
        item = random.randint(0, 4)
        tmp_record[item] = set_error(tmp_record[item])
        count_err += 1
        
    name, surname, addres, phone, index = tmp_record
    buf_record.append(record(name, surname, addres, region, phone, index))

print(buf_record)