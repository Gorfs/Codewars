def to_camel_case(text: str) -> str:
    '''
    input -> takes in a text in snake_case
    output -> text in camelCase
    desc -> takes text in snake_case and converts it to camel case
    '''
    if text == "":
        return "" #the input is empty, return an empty string

    capital = False #function to dictate if the next letter is going to be a capital
    res = "" #the string we return in the end
    for item in text: 
        if item in ["-", "_"]:
            capital = True
        else:
            if capital == True:
                res += item.upper()
                capital = False
            else:
                res += item
    return res
