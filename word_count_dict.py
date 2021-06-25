#Sentence --> input, keyword, value ->len of word
sentence = input('Enter your sentence: ')
#twinkle twinkle little star      
words = sentence.split(' ')
count_words = {word:len(word) for word in words}
print(count_words)
