word = input("Input a word: ")
 counter = 0
 for character in word:
     if counter%2 == 0:
         print(character, end=' ')
     counter+=1
