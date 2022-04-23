def disemvowel(s):
    return "".join([s[x] for x in range(len(s)) if s[x].lower() not in ['a','e','i',"o",'u']])

print(disemvowel("This website is for losers LOL!"))