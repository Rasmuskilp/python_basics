# declare some strings

# prompt user for his/her name
prompt_name = input('what is your name?')
# Save it to some variables with good names
name_1 = prompt_name

# prompt the user for some random number between 0 - 99
prompt_num = input('enter number between 0-99')
# store it in a variable called: user_chosen_num
user_chosen_num = prompt_num

# print a nice welcome message using user name
print(f'welcome to python {name_1}!')

# request the users last_name
prompt_last_name = input('WHat is your surname?')
last_name = prompt_last_name
# Print a nice message welcoming the user using their first and last name
print(f'Welcome {name_1} {last_name}')
# As for the users age
prompt_age =input('what is your age?')
age = prompt_age

# print a message of the users age and what year they were born in
print(f'Your age is {age} and your date of birth is : {2019-int(age)}')
# Compare the users input to the number they chose at the start and compare it
print(f'your chosen number was {float(user_chosen_num) - float(age)} different from your age ')
