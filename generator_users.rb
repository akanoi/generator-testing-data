ERR_NUMBER_PARAMETERS= 'A small number of input parameters!'
ERR_REGION_NAME = 'Invalid region name! (US, RU, BY)'
ERR_NUMBER_RECORDS = 'Invalid number records! (1..10.000.000)'
ERR_NUMBER_ERRORS = 'Invalid number errors! (>= 0)'


def get_input()
    if ARGV.length != 3 then 
        raise ERROR_IN_MES
    end

    if (ARGV[0] =~ /"BY|RU|US"/) == 0 then
        raise ERR_REGION_NAME
    end
    
    if (ARGV[1].to_i  < 1) or (ARGV[1].to_i > 10_000_000) then
        raise ERR_NUMBER_RECORDS
    end
    
    if ARGV[2].to_i < 0 then
        raise ERR_NUMBER_ERRORS
    end

    return ARGV[0], ARGV[1], ARGV[2]
end


(region, records_n, errors_n) = get_input()

puts region, records_n, errors_n




