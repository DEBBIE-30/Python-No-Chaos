number = int(input("Input a number(-1 to stop): "))
 counter = 1
 total = 0
 while number != -1:
     total+=number
     running_average = total/counter
     counter+=1
     print(f"The average is {running_average}")
     user_input = int(input("Input a number(-1 to stop): "))
