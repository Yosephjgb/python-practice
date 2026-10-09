# print("Hisssssss...")
# print("I am a \"Strong good man\"\n","I AM JGB","I HAVE GOD\n\"",  end="!!!")
# print("\nhi jgb" , " are you ok" , end="?",sep=",")

# print(0x123)

# print(0.0000000000000000000001)

# print('I\'m Monty Python.')

# print("\"I'm\"",'\n""learning""','\n"""Python"""')

# a = 6
# b = 3
# a //= 2 * b
# print(a)

# a = 6
# b = 3
# a /= 2 * b
# print(a)
# hi = input() 
# print("anything" , hi , "yeah")



# y=8/8
# print(y)

# print("*" * 10 )
# print(("*" + " " * 8 + "*" + "\n" ) * 5 , end="")
# print("*" * 10   )

# #input and type casting

# # num1 = int(input("Enter number "))
# # result = num1 ** 2
# # print("the squre of ", num1 , " is" , result)

# #concatenation of string
# name = "JGB" 
# age = " 23"
# print(name * 3)


# num1 = int(input("enter number num1"))
# num2 = int(input("enter number num2"))
# num3 = int(input("enter number num3"))

# if num1 > num2:
#     largest_num = num1
# elif num2 > num3:
#     largest_num = num2
# else:
#     largest_num = num3
# print("The largest Number is:" , largest_num)


# # Store the current largest number here.
# largest_number = -999999999

# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# print("hi jgb")
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(0, 11):
#     if i % 2 != 0:
#         print(i)

# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1

# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

# for digit in "0165031806510":
#     if digit == "0":
#         digit = "x"
#     print(digit, end="")

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

# n = range(4)
 
# for num in n:
#     print(num - 1)
# else:
#     print(num)

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
numbers[1] = numbers[4] 
print("New list contents: ", numbers)  # Current list contents.
print("number length:", len(numbers))  # Printing the length of the list. 
del numbers[1]
print(len(numbers))
print(numbers)
print(numbers[-1])

hat_list = [1, 2, 3, 4, 5]
hat_list[2] = int(input("Enter a number to replace: "))


# Write a line of code that removes the last element from the list.
del hat_list[-1]

# write a line of code that prints the length of the existing list.
print(hat_list)
print(len(hat_list))


numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

my_list = []  # Creating an empty list.

for i in range(6):
    my_list.append(i )

print(my_list)


my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]
    print(total)
print(total)