def zero(value=[0]): #your code here
    if value[0] == "*":
        return 0
    elif value[0] == "-":
        return 0 - value[1]
    elif value[0] == "+":
        return 0  + value[1]
    else:

        return 0


def one(value=[1]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return value[1]
    elif value[0] == "-":
        return 1 - value[1]
    elif value[0] == "+":
        return 1  + value[1]
    else:
        return 1 // value[1]

def two(value=[2]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 2 * value[1]
    elif value[0] == "-":
        return 2 - value[1]
    elif value[0] == "+":
        return 2  + value[1]
    else:
        return 2 // value[1]



def three(value=[3]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 3* value[1]
    elif value[0] == "-":
        return 3 - value[1]
    elif value[0] == "+":
        return 3  + value[1]
    else:
        return 3 // value[1]


def four(value=[4]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 4*value[1]
    elif value[0] == "-":
        return 4 - value[1]
    elif value[0] == "+":
        return 4  + value[1]
    else:
        return 4 // value[1]

def five(value=[5]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 5*value[1]
    elif value[0] == "-":
        return 5 - value[1]
    elif value[0] == "+":
        return 5  + value[1]
    else:
        return 5 // value[1]

def six(value=[6]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 6*value[1]
    elif value[0] == "-":
        return 6 - value[1]
    elif value[0] == "+":
        return 6  + value[1]
    else:
        return 6 // value[1]

def seven(value=[7]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 7*value[1]
    elif value[0] == "-":
        return 7 - value[1]
    elif value[0] == "+":
        return 7  + value[1]
    else:
        return 7 // value[1]


def eight(value=[8]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 8*value[1]
    elif value[0] == "-":
        return 8 - value[1]
    elif value[0] == "+":
        return 8  + value[1]
    else:
        return 8 // value[1]

def nine(value=[9]): #your code here
    if len(value) == 1:
        return value[0]
    if value[0] == "*":
        return 9*value[1]
    elif value[0] == "-":
        return 9 - value[1]
    elif value[0] == "+":
        return 9  + value[1]
    else:
        return 9 // value[1]

def plus(value): #your code here
    '''
    returns a list with the first value being a symbol and the second being a number
    '''
    return ["+" , value]
def minus(value): #your code here
    '''
    returns a list with the first value being a symbol and the second being a number
    '''
    return ["-" , value]
def times(value): #your code here
    '''
    returns a list with the first value being a symbol and the second being a number
    '''
    return ["*" , value]
def divided_by(value): #your code here
    '''
    returns a list with the first value being a symbol and the second being a number
    '''
    return ["/" , value]