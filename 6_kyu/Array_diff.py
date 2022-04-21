


def array_diff(a, b) -> list:
  '''
  input -> 2 lists, 
  output -> one list
  desc -> takes the first list and removes all the values of b in the list
  '''
  result_arr = []
  for elmt in a:
    if elmt not in  b:
      result_arr.append(elmt)
  return result_arr


print(array_diff([1,2,3], [1, 2]))