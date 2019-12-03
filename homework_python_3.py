# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # hero_name, hero_age, start, middle and end
story1 = {'hero_name' : 'tom','hero_age' : '54','start' :'the beginning','middle' : 'the highpoint', 'end' : 'the cliffhanger'}

#2 - Print the entire dictionary
print(story1)
#3 - Print the type of your dictionary
print(type(story1))
#4 - Print only the keys
print(story1.keys)
#4 - print only the values
print(story1.values)
#5 - print the individual values using the keys (individually, lots of printi commands)
print(story1['hero_name'])
#6 - Now let's reassing the exist key value pairs with user inputs
    # - hero_name, hero_age, hero_power
story1['hero_name'] = 'Gary'
print(story1)

#7 print the story in an organised/formated manor
print(story1['start']+' '+'of the story is before the'+' '+ story1['middle']+' '+ 'and the '+' '+ story1['end']+' '+
'is right at the end, the hero of the story is:'+' '+story1['hero_name']+' '+'and their age is'+' '+story1['hero_age'])