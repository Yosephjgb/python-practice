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

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.
 
# numbers[0] = 111
# numbers[1] = numbers[4] 
# print("New list contents: ", numbers)  # Current list contents.
# print("number length:", len(numbers))  # Printing the length of the list. 
# del numbers[1]
# print(len(numbers))
# print(numbers)
# print(numbers[-1])

# hat_list = [1, 2, 3, 4, 5]
# hat_list[2] = int(input("Enter a number to replace: "))


# # Write a line of code that removes the last element from the list.
# del hat_list[-1]

# # write a line of code that prints the length of the existing list.
# print(hat_list)
# print(len(hat_list))


# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
# numbers.append(4)

# print(len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)

# my_list = []  # Creating an empty list.

# for i in range(6):
#     my_list.append(i )

# print(my_list)


# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]
#     print(total)
# print(total)

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in my_list:
#     total += i

# print(total)

# my_list = [10, 20, 30, 40, 50]
# length = len(my_list)
# for i in range(my_list // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# print(my_list)
 
# #Note:

# # we've assigned the length variable with the current list's length (this makes our code a bit clearer and shorter)
# # we've launched the for loop to run through its body length // 2 times (this works well for lists with both even and 
# #      odd lengths, because when the list contains an odd number of elements, the middle one remains untouched)
# # we've swapped the ith element (from the beginning of the list) with the one with an index equal to (length - i - 1) 
# #      (from the end of the list); in our example, for i equal to 0 the (length - i - 1) gives 4; for i equal to 1, it 
# #      gives 3 ‒ this is exactly what we needed.


# # step 1
# beatles = []
# print("Step 1:", beatles)


# # step 2
# print("Step 2:", beatles)
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# # step 3
# print("Step 3:", beatles)
# for i in range (2):
#     name = input("add Stu Sutcliffe & Pete Best: ")
#     beatles.append(name)

# # step 4
# print("Step 4:", beatles)
# del beatles[-1]
# del beatles[-1]
# # step 5
# beatles.insert(0,"Ringo Starr")
# print("Step 5:", beatles)


# # testing list legth
# print("The Fab", len(beatles))

# lst = [1, [2, 3], 4]
# print(lst[1])
# print(len(lst))
 

# bubbleSort = [10,5,2,6,8]
# sawapped = True

# while sawapped:
#     sawapped = False

#     for i in range(len(bubbleSort) - 1):
#         if bubbleSort[i] > bubbleSort[i+1]:
#             sawapped = True
#             bubbleSort[i] , bubbleSort[i+1] = bubbleSort[i+1],bubbleSort[i]
# print(bubbleSort) 

# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))

# for i in range(num):
#     val = int(input("Enter a list element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)


# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# # Write your code here.
# #
# updated_list = []

# for i in my_list:
#     if i not in updated_list:
#         updated_list.append(i)
   
# my_list = updated_list
# print("The list with unique elements only:")
# print(my_list)

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #

# hot_days = 0

# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1

# print(hot_days, "days were hot.")

# # Cube - a three-dimensional array (3x3x3)

# cube = [[[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':(', 'x', 'x']],

#         [[':)', 'x', 'x'],
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],

#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]

# print(cube)
# print(cube[0][0][0])  # outputs: ':('
# print(cube[2][2][0])  # outputs: ':)'

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)


# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(0, n):
#         strange_list.insert(0, i)
    
#     return strange_list

# print(strange_list_fun(5))

# def is_year_leap(year):
#     #
#     # Write your code here.
#     #
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4  == 0:
#         return True
#     return False

# def days_in_month(year, month):
#     #
#     # Write your new code here.
#     #
#     if month < 1 or month > 12:
#         return None
    
#     if month == 2:
#         if is_year_leap(year):
#             return 29
#         return 28
#     if month in (1,3,5,7,8,10,12):
#         return 31
#     else:
#         return 30

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# def day_of_year(year, month, day):
#     # Check whether the month is valid
#     month_days = days_in_month(year, month)
#     if month_days is None:
#         return None

#     # Check whether the day is valid
#     if day < 1 or day > month_days:
#         return None

#     # Start with the current day
#     day_number = day

#     # Add the days in previous months
#     for m in range(1, month):
#         day_number += days_in_month(year, m)

#     return day_number


# print(day_of_year(2000, 12, 31))  # 366


# def is_prime(num):
#     # the for loop
#     for i in range(2,num):
#         # the if statement
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()


# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()


# def liters_100km_to_miles_gallon(liters):
#     #
#     # Write your code here.
#     #
#     return 235.214583 / liters

# def miles_gallon_to_liters_100km(miles):
#     #
#     # Write your code here.
#     #
#     return 235.214583 / miles

# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))

# def hi_everybody(my_list):
#     for name in my_list:
#         print("Hi,", name)

# hi_everybody(["Adam", "John", "Lucy"])

# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list

# print(create_list(5))

# def hi():
#     return
#     print("Hi!")

# hi()

# def is_int(data):
#     if type(data) == int:
#         return True
#     elif type(data) == float:
#         return False

# print(is_int(5))
# print(is_int(5.0))
# print(is_int("5"))

# def even_num_lst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst

# print(even_num_lst(11))

# def list_updater(lst):
#     upd_list = []
#     for elem in lst:
#         elem **= 2
#         upd_list.append(elem)
#     return upd_list

# foo = [1, 2, 3, 4, 5]
# print(list_updater(foo))

# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254


# def lb_to_kg(lb):
#     return lb * 0.4535923


# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
#         return None

#     return weight / height ** 2


# print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))



# # We've negated the condition (reversed the relational operators and
# # replaced ors with ands, receiving a universal expression for testing triangles).
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

# # Triangles and the Pythagorean theorem
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Enter the first side\'s length: '))
# b = float(input('Enter the second side\'s length: '))
# c = float(input('Enter the third side\'s length: '))

# if is_a_triangle(a, b, c):
#     print('Yes, it can be a triangle.')
# else:
#     print('No, it can\'t be a triangle.')


# #factorial function

# from itertools import product


# def factorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1

#     product = 1
#     for i in range(2, n + 1):
#         product *= i

#     return product
     
# for n in range(1, 6):
#     print(n, factorial(n))
    
# # Fibonacci numbers function
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))

# #recusrion on fibonacci and factorial functions
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)


#tuples

empty_tuples = ()
normal_tuples = (1, 2, 3)
short_tuples = 1, 2, 3
short_tuples_with_dot = 1.,
not_tuples = 1.  # This is not a tuple, it's an integer
print(empty_tuples)
print(normal_tuples) 
print(normal_tuples[0:-1])     
print(short_tuples)
print(short_tuples_with_dot)
print(not_tuples)

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

#dictionaries

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

#Let's now have a look at a dictionary method called items(). The method returns tuples (this is the first example where tuples 
# are something more than just an example of themselves) where each tuple is a key-value pair.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)

#Adding a new key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

#update() method
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)

#removing a key-value pair
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
#using pop() method
dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}

#creating a tuples using tuple() constructor
my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
#update() lets you merge dictionaries into one dictionary.
for item in (d1, d2):
    d3.update(item)

print(d3)

# my_list list to a tuple.
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

#colors tuple to a dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)


#tricky function
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))

