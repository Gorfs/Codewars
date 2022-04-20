def is_sum_of_cubes(s):
    #  return "n0 n1 sum(n) Lucky"
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result_numbers = []
    end_result_numbers = []
    end_string = ""
    ignore_counter = 0
    sum_of_all = 0

    for i in range(len(s)):
      if ignore_counter > 0:
        ignore_counter -= 1
        pass
      else:
        number = ""
        #print("currently looking at " , s[i])
        if s[i] in numbers:
          j = i 
          while s[j] in numbers and len(number)<3:
            number += s[j]
            #print("number building up is " , number)
            j +=1
          print("numba found is " , number)
          result_numbers.append(number)
          #preventing dups of numbers
          ignore_counter = len(number) -1
          number = ""
    #end case scenario
    if len(result_numbers) == 0:
      return 'Unlucky'


    #in result_numbers we now have all the numbers in the string
    print("starting cubic bit of this")
    for number in result_numbers:
      digits = []

      for char in number:
        digits.append(char)
      
      number_sum = 0

      for char in digits:
        number_sum += int(char)**3
      print(number_sum)

      if number_sum == int(number):
        #the number is cubic
        end_result_numbers.append(number)

    for number in end_result_numbers:
      end_string += number + " "
      sum_of_all += int(number)
    
    
    end_string += str(sum_of_all) + ' '
    end_string += "Lucky"
    return end_string


print(is_sum_of_cubes("&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()"))