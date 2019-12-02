#strings
## define strings
my_string = "I'm a string"
my_string2 = 'Me too'
print(my_string)
print(type(my_string2))
# concatenation - joining of two strings
print(my_string+' '+'but so am i'+' '+'and'+' '+my_string2)
print('these are examples of strings',my_string2,my_string)
concatenate = my_string + my_string2
print(concatenate)
#interpolation
age = 55
nom = 'juliette'
#these two statements need interpolation
print('welcome <person>, you are <age_years> old')
print('welcome <person>, you were born on the year <date_birth>')
#this is our actual interpolation
print(f'welcome {nom}, you are {age} old')
print(f'welcome {nom}, you were born on the year {2019 - age}')
print('welcome {}, you were born on the year {}'.format(nom,age))
##useful methods for strings
example_string = "       HELLoo             "
print(example_string)
#removes trailing white spaces
print(example_string.strip())
#counts the number of characters specified
print(example_string.count('L'))
#lower decapitalises
print(example_string.lower())
#upper capitalises
print(example_string.upper())
#capitalises the 1st letter
print(example_string.strip().capitalize()) # chaining methods
# standard builtin function len()
print(len(example_string))
#learning and using .split()
#.split(), splits the item into seprate strings, by using the specified delimiter
text_to_split = ('this is some example text in our file')
results_split = text_to_split.split(' ')
print(results_split)
#Castin and int
str_string = '1990'
#type tells you the type of the variable i.e string,int, flaot
print(type(str_string))
int_number = int(str_string)
print(type(int_number))
#int --> str
new_str = str(int_number)
print(new_str)