def is_valid_walk(walk):
    distance = [0,0]
    for i in range(len(walk)):
        if walk[i] == "n":
            distance[0] += 1
        elif walk[i] == "s":
            distance[0] -= 1
        elif walk[i] == "e":
            distance[1] +=1
        else:
            distance[1] -= 1
    if len(walk) == 10 and distance == [0,0]:
        return True
    else:
        return False
    