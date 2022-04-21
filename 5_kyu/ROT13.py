def rot13(message):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",'u',"v","w", "x","y","z"]
    alphabet_upper = []
    #just reducing time since I don't want to rewrite the alphabet twice ffs
    for elmt in alphabet:
        alphabet_upper.append(elmt.upper())
    
    if len(message) == 0:
        return ""
    else:
        res = []
        for letter in message:
            #upper vs lower if statement
            if letter in alphabet:
                if (alphabet.index(letter)+13) > len(alphabet)-1:
                    index = alphabet.index(letter)+13 - len(alphabet)
                    print(alphabet[index])
                    res.append(alphabet[index])
                else:
                    index = alphabet.index(letter)+13
                    res.append(alphabet[index])
                    print(alphabet[index])
            elif letter in alphabet_upper:
                if (alphabet_upper.index(letter)+13) > len(alphabet_upper)-1:
                    index = alphabet_upper.index(letter)+13-len(alphabet_upper)
                    res.append(alphabet_upper[index])
                else:
                    res.append(alphabet_upper[alphabet_upper.index(letter)+13])
            else:
                res.append(letter)
    print(''.join(res))
    return ''.join(res)                
        