#!/usr/bin/python3
word = "Holberton"
word_length = len(word); word_first_3 = word[0:3]
word_last_2 = word[word_length - 2:word_length]
middle_word = word[1:word_length - 1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
