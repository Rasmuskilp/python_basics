#numerical types
#numerical types are integers,floats,composites, big ints and complex number
#declaring an int
num1 = 20
print(type(num1))
num2 = 30.0
print(type(num2))
##Mathematical operators --- thesetake priority over logical operators, however use brackets to be sure
# +, -, *, %, /
result1 = 10 + 12 #adding
result2 = 10 -2 # subtracting
result3 = 10 * 30 # multiplying
result4 = 20 % 2 # finding the reminder
result5 = 20 / 5 # dividing

print(result1,result2,result3,result4,result5)
##Logical operators --> they
# one = is assignment
num_a = 10
num_b = 10
num_c = 13
# more than >
#less than <
#bigger than --> returns a boolean (bool)
print(num_b > num_c)
print(num_c > num_a)
#smaller than
print(num_b < num_c )
print(num_c < num_a)
#bigger.smaller or equal
print (num_a >= num_b)
print(num_c >=num_a)
print(num_b >= num_c)
print((num_a + num_c) > num_b)
#check if the same data type
print('10' == 10)
print(num_b == num_a)
print(num_a == num_c)
#Boolean - are True or False
#own datatype
print(type(True))
print(type(False))
bool_var = True
false_var = False
print(bool_var == false_var)
print(bool_var != false_var)
#Logical AND & logical OR
#and syntax - (<operation> and <condition>) --> bool
#requires the two sides to be true to return true
print(True and True)
print(True and False) # only one side is true, therefore it is false
#Logical <or>
# necessitates only one side to be true to return true
print(True and True) # both sides true --> true
print(True and False) # one side is true --> true
