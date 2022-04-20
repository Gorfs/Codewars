from re import I


import math

def find_next_square(sq):
  if sq**0.5 != int(sq**0.5):
    return -1
  else:
    i = sq + 1
    while i**0.5 != int(i**0.5):
      i += 1
  return i

print(find_next_square(114))