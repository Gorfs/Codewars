def find_it(seq):
    '''
    input -> list of ints
    output -> int
    desc -> takes a list of int and returns the integer that 
    apears in the list an odd amount of times
    '''
    dic = {} # making a dictionary that has the keys being each number in the array
                # and the values being the amount of times it is seen in the list
    for number in seq:
        if seq.count(number) % 2 != 0:
            return number
    return None