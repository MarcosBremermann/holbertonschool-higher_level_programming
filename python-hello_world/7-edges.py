#!/usr/bin/python3
word = "Holberton"
s=word.replace(" ", "").replace("\t", "").replace("\n", "")
word_first_3 = s[0:3]
word_last_2 = s[7:9]
middle_word = s[1:8]
print(f"First 3 letters: {word_first_3}\nLast 2 letters: {word_last_2}\nMiddle word: {middle_word}")

