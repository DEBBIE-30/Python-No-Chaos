for counter in range(100,1000):
    
     digit_one = counter%10
     digits_two = (counter//10)%10
     digits_three = (counter//100)
     if (digit_one**2 + digits_two**2 + digits_three**2 == counter):
         print(counter, end=' ')
     else:
         continue
