

def validSolution(solution):
    #step 1 checking each square
    print("input = " , solution)
    arr_squares = []
    for i in range(0, 9, 3): 
        #this should iterate between 0, 3, 6,
        #there for we can use this as our horizontal spacer
        for j in range(0, 9 , 3):
            square = []
            #this should take the same iterations, between 0,3,6
            #this will be our vertical spacer
            square.append(solution[i][j])
            square.append(solution[i][j+1])
            square.append(solution[i][j+2])
            square.append(solution[i+1][j])
            square.append(solution[i+1][j+1])
            square.append(solution[i+1][j+2])
            square.append(solution[i+2][j])
            square.append(solution[i+2][j+1])
            square.append(solution[i+2][j+2])
            arr_squares.append(square)
    for elmt in arr_squares:
        if 0 in elmt or len(elmt) != len(set(elmt)):
            print("squares not right" , arr_squares ,"specifically", elmt)
            return False


    #step 2 checking all horizontal lines
    for line in solution:
        if 0 in line or len(line) != len(set(line)):
            print("horizontal lines not right" , line , elmt)
            return False


    #step 3 checking all vertical lines
    lines_arr = []
    line = []
    for i in range(9):
        #vertical spacer
        for j in range(9):
            #horizontal spacer
            line.append(solution[j][i])
        
        lines_arr.append(line)
        line = []

    for elmt in lines_arr:
        #print("lines elmt = " , lines_arr)
        if 0 in elmt  or len(elmt) != len(set(elmt)):
            #print("vertical lines not right" , lines_arr ," specifically ", elmt)
            return False

    return True
    
        



print(validSolution([[1, 3, 2, 5, 7, 9, 4, 6, 8], 
                    [4, 9, 8, 2, 6, 1, 3, 7, 5], 
                    [7, 5, 6, 3, 8, 4, 2, 1, 9], 
                    [6, 4, 3, 1, 5, 8, 7, 9, 2], 
                    [5, 2, 1, 7, 9, 3, 8, 4, 6], 
                    [9, 8, 7, 4, 2, 6, 5, 3, 1], 
                    [2, 1, 4, 9, 3, 5, 6, 8, 7], 
                    [3, 6, 5, 8, 1, 7, 9, 2, 4], 
                    [8, 7, 9, 6, 4, 2, 1, 3, 5]]))