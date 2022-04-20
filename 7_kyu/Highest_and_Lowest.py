def high_and_low(numbers) -> str:
  '''
  takes a string of intergers and returns the biggest and smallest number of that string
  '''
  #making a list of numbers
  numbers = numbers.split(' ')
  numbersInt = []
  for number in numbers:
    numbersInt.append(int(number))

    
  return str(max(numbersInt)) + " " + str(min(numbersInt))
  

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))