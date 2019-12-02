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
##useful methods for strings
