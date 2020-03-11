import itertools

#get the dictionary file
with open('all_the_words.txt') as file:
      contents = file.read()

#ask for input
things = int(input("How many things are there? "))

print("Okay, there are ", things, "number of things")

#creating a variable to keep track of the number of words
words_Ive_entered = 0

#something
while things > words_Ive_entered:
  print("Give me a word")
  word1 = str(input())
  words_Ive_entered = words_Ive_entered+1
  print("You have entered", words_Ive_entered,"word(s)")
  char_in_word = list(word1)
  print(char_in_word)

#what????
  possibilities = list(itertools.permutations(word1, r=None))
  for elem in possibilities:
      print(elem)
      if elem in contents:
        print ('word found')
      else:
        print ('word not found')
