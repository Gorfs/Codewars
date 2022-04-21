def max_ball(v0):
    #basic inputs for the formula of the speeeeeeeeed
    #you have to convert all the mesurements or it won"t work
    v = v0/36
    g = 0.0981
    height = 0
    max_height = 0
    #need the I to count the tenths of seconds
    t=0
    while height >= max_height:
        t += 1
        height = (v*t) - (0.5*g*t*t)
        if height > max_height:
            max_height = height
    return t-1
    
   