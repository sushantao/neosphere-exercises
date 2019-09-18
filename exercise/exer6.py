#Write a program that accepts a comma separated sequence of words 
# as input and prints the words in a comma-separated sequence 
# after sorting them alphabetically.

my_words=input("Enter words")
words=my_words.split(",")
words.sort()
print(words)
print(",".join(words))