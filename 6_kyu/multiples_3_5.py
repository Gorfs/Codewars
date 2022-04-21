def solution(number):
    number_divisable = []
    for i in range(0 ,number):
        if i % 3 == 0 or i% 5 ==0:
            if i == number:
                return sum(number_divisable)
            else:
                number_divisable.append(i)
    return sum(number_divisable)
            
  