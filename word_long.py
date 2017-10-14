sentence = raw_input("Enter sentence: ")
words = sentence.split(" ")
maxlen = 0
longest_word = ''
for word in words:
    if len(word) >= maxlen:
          maxlen = len(word)
          longest_word = word
print(longest_word, maxlen)
