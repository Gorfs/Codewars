def reverse_words(text):
  reversed_words = []
  reversed_word = ""
  words = []
  word = ""
  for i in range(len(text)):
    if text[i] == " ":
      words.append(word)
      word = ""
    else:
      word += text[i]
      
  words.append(word)
    
  for word in words:
    for j in range (1, len(word) +1):
      reversed_word += word[-j] 
    reversed_words.append(reversed_word)
    reversed_word = ""
  return ' '.join(reversed_words)

print(reverse_words('The quick brown fox jumps over the lazy dog.'))



    