def delete_nth(order, max_e):
    count = {}
    for i in range(len(order)):
        if order[i] not in count:
            count[order[i]] = 0
    result_arr = []
    for num in order:
        print(count[num])
        if count[num] < max_e:
            result_arr.append(num)
            count[num] += 1
    return result_arr



print(delete_nth([20,37,20,21], 1))