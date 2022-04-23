from itertools import permutations

def next_bigger(n):
    '''
    Starting from the right, find the first digit that has at least one smaller digit to its right. We'll call that digit X.
    Then find the largest digit that is to the right of X, and is smaller than X. We'll call that digit Y.
    Swap X and Y. This makes the number smaller.
    Then sort all of the digits to the right of Y in descending order. This makes the number as big as possible, without making it bigger than the original.
    '''
    digits = [int(i) for i in str(n)]
    if len(str(n)) > 5:
        print("values inputed = " , digits)
        X = len(digits)-1
        Y = 0
        found = False

        for j in range(len(digits)-1,0,-1):
            print("X could be " , j)
            if digits[j-1] < digits[j] and found == False:
                X = j-1
                found = True
        #print("X = " , X)
        
        if Y == len(digits):
            print("value inputed " , digits, "has no smaller value")
            return -1
        else:
            #code to find Y 
            max_index = X + 1

            for k in range(len(digits)-1,X,-1):
                #print("k = " , k)
                if digits[k] > digits[X] and digits[k] < digits[max_index]:
                    max_index = k
        Y = max_index
        if X == len(digits) - 1:
            return -1
        print("X = " , X , " and Y = " , Y)
        digits[X], digits[Y] = digits[Y] , digits[X]
        print("swapped : ", digits)

        if Y == len(digits)-1 and X == len(digits) - 2:
            return lst_to_int(digits)


        values_to_sort = []
        for i in range(Y + 1, len(digits)):
            values_to_sort.append(digits[i])
        print("sorting" , values_to_sort)
        values_to_sort.sort()
        print("sorted " , values_to_sort)

        for l in range(len(values_to_sort)):
            digits[X + l+ 1] = values_to_sort[l]

        if len(str(lst_to_int(digits))) != len(str(n)):
            print("value inputed " , digits, "has no smaller value")
            return -1
        
        return  lst_to_int(digits)


    else:
        arr = list(permutations(digits))
        arr.sort()
        #print(arr)

        for elmt in arr:
            value = []
            int_value = 0
            for item in elmt:
                value.append(item)
            for i in range(len(value)):
                int_value += value[i]*(10**(len(value) - i - 1))
            #print(int_value , value)

            print(int_value)

            if int_value > n and len(str(int_value)) == len(str(n)):
                print("returning a value: ", end="")
                return (int_value)
        return -1

def lst_to_int(digits):
    result = 0
    for i in range(len(digits)):
        result += digits[i]*(10**(len(digits) -i-1))
    return result

print(next_bigger(9876543210))
'''
IT WORKS
'''