def ascend_descend(length, minimum,maximum):
    possible_answers = []
    for i in range(maximum - minimum + 1): 
        possible_answers.append(minimum + i) #now possible answers should have every number between minimum and maximum
    for j in range(1,maximum - minimum):
        possible_answers.append(maximum - j) # now possible answers should just be the repeatable string until length
    print(possible_answers)
    res = ""
    for k in range(length):
        l= k % len(possible_answers)
        res += str(possible_answers[l])
    return res


print(ascend_descend(11, 0, 4))

