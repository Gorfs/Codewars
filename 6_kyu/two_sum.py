def two_sum(numbers, target):
    for i in range (len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target and i != j:
                return (i , j)