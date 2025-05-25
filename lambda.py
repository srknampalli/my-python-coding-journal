# students = [("Alice", 88), ("Bob", 75), ("Charlie", 95), ("David", 85)]
# sorted_students = sorted(key=lambda item: item[1],students)
# print(sorted_students)  # Output: [('Bob', 75), ('David', 85), ('Alice', 88), ('Charlie', 95)]

# #Addition
# add = lambda a,b,:a**b
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted_xs = sorted(xs.items() ,key=lambda item : item[1])
print(sorted_xs)
# params = (4,2)
# res= add(*params)
# print(res)

# def add(a,b,c):
#     print(a+b+c)

# add(1,8,9)

#MAX NUMbBER FINDING

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5,15,16]

# max_number = max(numbers, key=lambda x: x)

# # print(max_number)


# # second largest

# numbers.remove(max_number)

# second_max = max(numbers)

# print(second_max)





#Sorted method with lamda


students = [("Alice", 88), ("Bob", 75), ("Charlie", 95), ("David", 85)]
# sorted_students = sorted(students, key=lambda student: student[0])
# print(sorted_students) 

s_stu = key = sorted(students ,key=lambda student:student[1])

#for descending order s_stu = sorted(students, key=lambda student: student[1], reverse=True)

# print(s_stu)


# #Sorting a List of Strings by Length
# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# sorted_fruits= sorted(fruits, key=lambda fruit : len(fruit), reverse=True )

# print(sorted_fruits)


#Sorting a List of Dictionaries by a Specific Key sort by age

# employees = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 35},
#     {"name": "David", "age": 28}
# ]

# sorted_emp = sorted(employees, key=lambda employee: employee["age"])
# print(sorted_emp)


#Sorting a List of Lists by the Last Element:
#Given a list of lists where each inner list contains a name and an ID number, sort the outer list by the ID number

# peoples = [["Alice", 3], ["Bob", 1], ["Charlie", 2], ["David", 4]]

# # print(peoples[1])


# sored_list = sorted(peoples, key= lambda people:people[1])

# print(sored_list)


#Sorting a List of Strings Alphabetically Ignoring Case:
#Given a list of strings, sort them alphabetically, ignoring case

# animals = ["elephant", "Dog", "cat", "Bear", "antelope"]

# sorted_ani = sorted(animals,key=lambda animal:animal.lower())

# print(sorted_ani)










# sorted_ani = sorted(animals, key= lambda animal:animal.lower())

# print(sorted_ani)

#Sorting a List of Tuples by the Sum of Elements:
#Given a list of tuples where each tuple contains two numbers, sort the list by the sum of the numbers in each tuple.

pairs = [(1, 20), (8, 4), (5, 9), (5, 7)]

opairs = sorted(pairs,key=lambda pair: pair[0]+pair[1])

print(opairs)
 
 








# sorted_pair = sorted(pairs, key=lambda pair:pair[0]+pair[1])

# print(sorted_pair)



#So, even though the lambda function only references pair[0] and pair[1], it's applied to each tuple in the list. The pair in the lambda function is a placeholder that represents each tuple in pairs as the sorted() function iterates through the list.

# dates = ["2023-01-01", "2021-12-31", "2022-07-23", "2023-06-15"]

# sorted_dates= sorted(dates,key=lambda date:date)

# print(sorted_dates)


# Sorting a List of Dictionaries by Nested Key:
# Given a list of dictionaries where each dictionary contains a name and another dictionary with 'scores' for different subjects, sort the list by the 'math' score.


# students_scores = [
#     {"name": "Alice", "scores": {"math": 88, "science": 92}},
#     {"name": "Bob", "scores": {"math": 75, "science": 78}},
#     {"name": "Charlie", "scores": {"math": 95, "science": 89}},
#     {"name": "David", "scores": {"math": 85, "science": 94}}
# ]

# sorted_scores= sorted(students_scores, key=lambda student_score:student_score["scores"]["math"])

# print(sorted_scores)


# fahrenheit = [32, 45, 64, 72, 91, 100]
# celsius = list(map(lambda x: (x - 32) * 5/9, fahrenheit))

# print(celsius)

words = ["hello", "world", "python", "programming"]

# capital_w = list(map(lambda word:word.upper(),words))

# print(capital_w)

op = list(map(lambda word:word.upper(),words))

# print(op)


numbers = [1, 2, 3, 4, 5]


opnum = list(map (lambda num:num**2,numbers))

print(opnum)




# sq_num= list(map(lambda num:num**2,numbers))

# print(sq_num)


# prices = [100, 200, 300, 400, 500]
# discount_rate = 0.10

# fixed_dis = list(map(lambda price: price-(price*discount_rate),prices))

# print(fixed_dis)

# Exercise 8: Convert List of Tuples
# Given a list of tuples where each tuple contains two numbers, use map and a lambda function to create a new list where each tuple contains the product of the two numbers.
# tuples = [(1, 2), (3, 4), (5, 6)]
# #res = list(map(lambda tuple:sum(tuple),tuples))
# res = list(map(lambda tuple:tuple[0] / tuple[1],tuples))
# print(res)
#Calculate Factorials
# import math
# numbers = [1, 2, 3, 4, 5]

# res = list(map(math.factorial, numbers))

# print(res)

# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]
# res = zip(list1,list2)
# list_res = list(res)
# print(list_res)



# # fin_res = list(map(lambda num:num[0]+num[1],list_res))

# # print(fin_res)

# res = list(map(lambda x,y: x+y, list1,list2))
# print(res)

# print_llm_reponse("what is the capital of Telangana")




# Exercise 1: Filter Even Numbers
# Given a list of numbers, use filter() and a lambda function to return a list containing only the even numbers.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_num = list(filter(lambda num : num%2==0,numbers))

# print(even_num)

# Exercise 2: Filter Strings of a Certain Length
# Given a list of strings, use filter() and a lambda function to return a list of strings that have more than 4 characters.

words = ["apple", "banana", "cat", "dog", "elephant", "fish"]

opowrds= list(filter(lambda word:  len(word) > 4,words))

print(opowrds)








# four_words = list(filter(lambda word:len(word)>4,words))

# print(four_words)


# Exercise 3: Filter Positive Numbers
# Given a list of integers, use filter() and a lambda function to return a list of positive numbers.

# args = [0, 8]


# res = list(range(*args))

# print(res)
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# sorted_pair = sorted(pairs, key=lambda pair: pair[1])

# print(sorted_pair)

# Exercise 4: Filter Words Starting with a Specific Letter
# Given a list of words, use filter() and a lambda function to return words that start with the letter 'a'.

# words = ["apple", "banana", "avocado", "grape", "orange"]

# li_words = list(filter(lambda word : word.startswith('o') , words))

# print(li_words)

# Exercise 5: Filter Palindromes
# Given a list of words, use filter() and a lambda function to return only the words that are palindromes (i.e., words that read the same forward and backward).

# words = ["level", "world", "radar", "hello", "madam", "python"]

# pa_words = list(filter(lambda word: word==word[::-1],words ))

# print(pa_words)

# words = "sai"

# print(words[::-1])
# my_set = {3, 1, 4, 1, 5, 9}
# print(my_set)

# Exercise 6: Filter Non-Empty Strings
# Given a list of strings, use filter() and a lambda function to return only the non-empty strings.

# strings = ["", "hello", "", "world", "", "python"]

# filtered_str = list(filter(lambda str:  str != "", strings))

# print(filtered_str)

# Exercise 7: Filter Students Based on Scores
# Given a list of tuples representing students and their scores, use filter() and a lambda function to return only the students who scored more than 50.
# students = [("John", 45), ("Emily", 75), ("Anna", 60), ("Mike", 30)]

# filter_students = list(filter(lambda student: student[1]>50,students ))
# print(filter_students)

# Exercise 8: Filter Multiples of 3
# Given a list of numbers, use filter() and a lambda function to return the numbers that are multiples of 3.
# numbers = [3, 6, 7, 8, 9, 12, 14, 15, 20, 21]

# fil_num = list(filter(lambda num : num%3==0,numbers))

# print(fil_num)

# Exercise 2: Concatenate Strings
# Given a list of strings, use reduce() and a lambda function to concatenate all the strings into a single string.
#from functools import reduce
# words = ["Hello", "world", "from", "Python"]

# res = reduce(lambda word1,word2: word1 + "_" + word2, words)

# print(res)

#Given a list of numbers, use reduce() and a lambda function to calculate the sum of the squares of all numbers.
# numbers = [2, 3, 4, 5]

# res = reduce(lambda a,b : a+b**2,numbers)

# print(res)












    
