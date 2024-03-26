import os
import logo

#example user:
fName = "Ashley"
lName = "Finch"

logo.title()
#welcome message
print("Welcome to the Old Cove Eatery!🍴")

#ask for the users name
fName = input("\nFirst name: ")
lName = input("Last name: ")

#ask for the users age
age = int(input("Age: "))

os.system("clear")
logo.title()

if age < 13:
  print("\u001b[31mYou must be 13 or older to order from the Old Cove Eatery.\u001b[0m")
elif age >= 13:
  print("Hello " + fName + " " + lName + "! I am your personal assistant!\n")

  order_num = int(input("Please enter your 5-digit Order Number: "))
  
  #ask for the users order number and restrict it to 5 digits
  while order_num < 10000 or order_num > 99999:
    print("\u001b[31mInvalid Order Number.\u001b[0m")
    
    #else continue with the program
    order_num = int(input("5-digit Order Number (located on reciept or mobile confirmation): "))

  print("\n#", order_num)
  #print choices and ask for the users choice
  print("\n1. Order Status")
  print("2. ___")
  print("3. ____") 
  print("4. Exit")
  
  #ask for the users order number for all choices expect choice 4
  #while loop for the choices 
  choice = int(input("\nHow may I help you today? (1-4): "))
  
  while choice > 4:
    print("\u001b[31mInvalid choice, please try again.\u001b[0m")
    choice = int(input("\nHow may I help you today? (1-4): "))

  #if statement based on user choice
  if choice == 1:
    print("hi")
  elif choice == 2:
    print("hey")
  elif choice == 3:
    print("hello")
  elif choice == 4:
    print("Thank you for visiting the Old Cove Eatery! Have a great day!😊")

    
#sources:
#https://www.geeksforgeeks.org/clear-screen-python/3/
#https://replit.com/@mrwatsonsst/ANSI-Escape-Colour-Codes-Python-Workaround?v=1#main.py
#https://www.geeksforgeeks.org/python-program-to-print-emojis
#https://www.youtube.com/watch?v=rfscVS0vtbw   (python full course)
