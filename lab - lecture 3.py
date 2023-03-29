#### Fix the following errors (in 1-6)!

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z += 'd'
print(z)

#5 Why does the x not display 10, followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
fav_colr = 'grey'
color = f'My favorite color is {fav_colr}, what is yours?'
print(color)

#### Answer the following questions without changing the code given

#7 Make the entries in this list unique
schools = ('harris', 'booth', 'crown', 'harris', 'harris')
schools = set(schools)
print(schools)
#8 Change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = list(animals)
print(animals)
animals[2] = 'cat'
print(animals)

#9 Make this string take a name based on a variable (you can modify the code on this one)
my_name = 'Jose'
welcome = f'Hello {my_name}, and welcome to Data and Programming!'
print(welcome)

#10 Separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'


print(my_sent.lower().split())

