word = input("Enter a word: ").lower().strip()
 vowel_counter = 0
 consonant_counter = 0
 for character in word:
     if character in 'aeiou':
         vowel_counter+=1
     else:
         consonant_counter+=1
 print(f"There are {vowel_counter} vowels in this word and {consonant_counter} consonants in this word")
