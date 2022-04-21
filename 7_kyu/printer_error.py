def printer_error(s):
    good_values = ["a" , "b" , "c" , 'd' , 'e' , 'f' ,'g', 'h', 'i' , 'j' , 'k' , 'l' ,'m']
    counter = 0
    for char in s:
        if char not in good_values:
            counter +=1
    return "{}/{}".format(counter, len(s))


print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))