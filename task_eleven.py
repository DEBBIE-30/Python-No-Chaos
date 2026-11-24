sentence = input("Enter a sentence: ")
 word = ""
 for character in sentence:
     if character != "":
         word+=character
     else:
         print(word)
         word = ""

