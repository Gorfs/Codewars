

def encryptor(key, message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    for char in message:
        if char.lower() in alphabet:
            upper = False
            if char.isupper():
                upper = True
            char_to_add_index = alphabet.index(char.lower()) + key
            if  char_to_add_index >= len(alphabet):
                while char_to_add_index > len(alphabet):
                    char_to_add_index -= len(alphabet) - 1
            if char_to_add_index < 0:
                while char_to_add_index < 0:
                    char_to_add_index += len(alphabet)
            print(char_to_add_index)
            if upper== False:
                result += alphabet[char_to_add_index]
            else:
                result += alphabet[char_to_add_index].upper()
        else:
            result += char
    return result
