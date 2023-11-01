#Tasks:
#Write a program that accepts user input to create a list of integers. 
#Then, compute the sum of all the integers in th
input_string = ('10 20 30 50 80 \n')
user_list = input_string.split()
print('string list: ', user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

print('User list: ', user_list)
# Calculating the sum of list elements
print("Sum = ", sum(user_list))

#Create a tuple containing the names of five of your favorite books. 
#Then, use a for loop to print each book name on a separate line.

 #Creating a Tuple
# Lisf of My book Datatype
My_books = ('Bible', 'kamusi', 'Dictionary', 'World', 'Earth')
print("\nList of My books")
print(My_books)

#Tuple for loop
print("\nTuple with a loop method1")
for item in My_books:
        print(item)

print("========================================")
print("\nTuple with a loop method2")
for index in range(len(My_books)):  
        print(My_books[index])

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.
print("\nDictionary to console")
person = {'first_name': 'Elon', 'last_name': 'Abdon', 'age': 43, 'favourate color': 'Yellow', } 
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['favourate color'])

#Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets
print("\ninput two set of integers")
numbers = {2,4,6,8,9,}
print('intial set:',numbers)
numbers.add(10)
print('update set:', numbers)

#Create a program that stores a list of words.
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
print("\nlist of use list comprehension creat new list that cointains only words have odd numbers")
languages = ('German', 'Italy', 'English')
numbers =   [1, 2, 3, 4, 5]
print(languages)
odd_numbers = []
for i in numbers:
  if i % 2 != 0:
    odd_numbers.append(i)
print(odd_numbers)



