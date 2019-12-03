#if functions
#part of control loop along with while function
#syntax
#if <condition>:
    #block of code
#elif <condition>
    #<block of code>
#else:
    #block of code>
age = int(input('what is your age?'))
#if stops at first true condition and then exits
#most specific has to be on top
# conditions are built with operators and logical operators
if age > 21:
    print('you can both vote and drink')
elif age <= 21 and age >= 18:
    print('you can vote but not drink in the USA')
# elif age >= 18:
#     print('you can vote, please register')
elif age >= 16:
    print('you can drive')
else:
    print('you can not do anything')