'''
______
PART 3
______
Write a program that asks the user to input one integer. The program will then print two strings, one stating if it's positive, negative, or zero, and another that states whether or not is is divisible by 3. (Hint: to check divisibility by 3, you will find using the modulus(%) operation very helpful.)

3 examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a number:  -2
negative
not divisible by 3

Enter a number:  0
zero
divisible by 3

Enter a number:  5
positive
not divisible by 3
'''

#write your code below
number = int(input("Enter a number:"))

if number < 0:
  print ("The number that you entered is negative.")
elif number > 0:
  print ("The number you entered is positive.")
elif number == 0:
  print ("The number you entered is zero.")
elif number % 3 == 0:
  print ("The number you entered is divisible by 3.")
elif number % 3 != 0:
  print ("The number you entered is not divisible by 3.")