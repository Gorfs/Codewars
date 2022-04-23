def is_interesting(number, awesome_phrases):
    '''
    a num is interesting if:
     a number is followed by all 0's ex: 1000 , 90000
     every digit is the same number  ex:1111 , 999
     the digits are incremental      ex:1234
     the digits are decrementing     ex:4321
     the digits are a palindrom      ex: 1221 , 73837
     the digits are in the awsome phrases list


     return should be:
        0: not interesting
        1:if the number is in 2 miles
        2:the number = number is interesting
    '''
    numbers_to_check = [number, number+1, number +2]
    #step 1 see if the numbers are above 3 digits
    for number in numbers_to_check:

        if number >= 100:
            #main loop to see all the number
            if str(number).count('0') == len(str(number))-1:
                #there is only one digits that is not a zero in the number
                #this number is interesting
                if numbers_to_check.index(number) == 0:
                    return 2
                return 1

            #check for sequential digits
            check_incremental = True
            for j in range(len(str(number))-1):
                try:
                    
                    if (int(str(number)[j]) + 1 != int(str(number)[j + 1])):
                        if (str(number)[j] == "9" and str(number)[j+1] == "0"):
                            pass
                        else:
                            check_incremental = False
                except:
                    check_incremental = False
                    print("Exception")
            if check_incremental == True:
                print("the number is incremental" , number)
                if numbers_to_check.index(number) == 0:
                    print("number is " , number)
                    return 2
                return 1

            check_decremental = True
            for k in range(len(str(number))-1):
                try:
                  
                    if (int(str(number)[k]) - 1 != int(str(number)[k + 1])):
                        if (str(number)[k] == "0" and str(number)[k-1] == '9' and str(number)[k-2] == "8"):
                            
                            pass
                        else:
                            print("exception")
                            check_decremental = False
                except:
                    print('exception' , str(number)[k])
                    check_decremental = False
            if check_decremental == True:
                print("the number is decremental")
                if numbers_to_check.index(number) == 0:
                    return 2
                return 1

            #check for palindrom
            check_palindrome = True
            for l in range(1,len(str(number)) + 1):
                if str(number)[l-1] != str(number)[len(str(number))-l]:
                    check_palindrome = False
            if check_palindrome == True:
                print("the number is palindrome")
                if numbers_to_check.index(number) == 0:
                    return 2
                return 1
            
            #check if number is in the awesome list
            if number in awesome_phrases:
                print(number, "the number is in awesome phrases")
                if numbers_to_check.index(number) == 0:
                        return 2
                return 1
            
        else:
            pass
    return 0
        
            

        

print(is_interesting(999997,[1337,256]))


    


            

