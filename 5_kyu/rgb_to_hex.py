#gets the rgb value and converts it to hex

def rgb(r, g, b):
    return "{}{}{}".format(to_hex(r) , to_hex(g), to_hex(b))
    
    

def to_hex(value):
    if value <= 0:
        return "00" 
    elif value > 255:
        return "FF"
    hexValues = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    result = value
    hexresult = ""
    #if result < 10:
        #return result

    while result > 0:
        #hexTemp is gonna be an int
        hexTemp = result%16
        #hex temp is alway gonna be smaller than 16
        hexTemp = hexValues[hexTemp-1]
        hexresult += hexTemp
        result = result//16
    
    if len(hexresult) < 2:
        print('hexresult = ' , hexresult , 'and its length is ' , len(hexresult))
        hexresult = "0{}".format(hexresult)
        return hexresult
    if hexresult == 0:
        return "00"
    #the hexResult will be reversed as we are appending to the end of the string instead of the start
    return "".join([hexresult[-i] for i in range(1,len(hexresult) + 1)])


print(to_hex(254))
print(rgb(254,253,252))