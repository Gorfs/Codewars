def bin_to_decimal(bin):
    '''
    surprises me that this is in 8kyu
    '''
    result = 0
    for i in range(len(bin)):
        if bin[i] == "1":
            result += 2**(len(bin)-1- i)
    return result

