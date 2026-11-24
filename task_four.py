word = input("Input a string: ")
 reversed_string = ""
 for character in word:
     reversed_string = character + reversed_string
 if reversed_string == word:
     print("This word is a palindrome")
 else:
     print("This word is not a palindrome")

