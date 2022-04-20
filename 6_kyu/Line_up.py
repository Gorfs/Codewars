#this is the Line up kata that is made by TureNoobMan

example = ["white has black on his left",
 "red has green on his right",
  "black has green on his left"]


def line_up(hints):
  result = []
  clues = []
  for hint in hints:
    print(result)
    #loops through all the hints
    splitHint = hint.split(' ')
    #the first value of splitHint is the subject, the 3rd is the next subject and the last is the direction
    subject1 = splitHint[0]
    subject2 = splitHint[2]
    if splitHint[-1] == "left":
      direction = -1
    else:
      direction = 1

    temp = []
    
    if subject1 not in result and subject2 not in result:
      result.append(subject1)
      index = result.index(subject1) + direction

      if index < 0:
        index = 0
      result.insert(index, subject2)
      temp.append(subject1)
      temp.insert(index, subject2)
      

    elif subject1 in result and subject2 in result:
      print("both subjects are in the result list")

      temp.append(subject1)
      if direction == 1:
        temp_index = 1
      else:
        temp_index = 0
      temp.insert(temp_index, subject2)
      print("temp is " , temp)
      
      if direction ==1:
        
      
      print(result)


    elif subject1 in result:
      index = result.index(subject1) + direction
      if index < 0:
        index = 0
      result.insert(index, subject2)

      temp.append(subject1)
      temp.insert(index, subject2)
    else:
      #subject 2 is in the list but not one
      index = result.index(subject2) + direction
      if index < 0:
        index = 0
      result.insert(index, subject1)
      temp.append(subject2)
      temp.insert(index, subject1)

    clues.append(temp)


 

    
print(line_up(example))
    

