# Lists!

# Define a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _numeric values from 0 to inf, where 0 corresponds item 1 in list______?????
X_mas = ['fat','black','cat','in','hat']

# Print the lists and check it's type
print(X_mas)
print(type(X_mas))

# Print the list's first object
print(X_mas[0])

# Print the list's second object
print(X_mas[1])

# Print the list's last object
print(X_mas[-1])

# Re-define the first item on the list and
X_mas[0] = 'lazy'

# Re-define another item on the list and print all the list
X_mas[2] = 'dog'
print(X_mas)

# Add an item to the list and print the list
X_mas.append('top')

# Remove an item from the list and print the list
X_mas.pop(2)
print(X_mas)
# Add two items to list and print the list
y = ['call', 'object']
x = 0
for i in y:
    X_mas.append(y[x])
    x = + 1
print(X_mas)