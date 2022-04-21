def changer(string):
    result = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a','e','i','o','u']
    for char in string:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower()) + 1
            if index == len(alphabet):
                index = 0
            if alphabet[index] in vowels:
                result += alphabet[index].upper()
            else:
                result += alphabet[index]
        else:
            result += char
        
    return result

print(changer("Cat30"))