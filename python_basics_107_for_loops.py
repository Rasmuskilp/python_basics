# For loops!
#fop loops will iterate over an iterable object and run a block of code
#syntax
#for <placeholder> in <iterable object> :
#indent
#doing stuff in this block
#more things in a block
#note:the block of code exist after the : (colon)
#it is the lines of codes that ARE INDENTED
#and it stops when the indenation stops
#iterables are lists,dictionaries and also strings(will see why later)
wish_list = ['rc car','molten cheese','cheerleaders','White shirts','sugar laces',"reese's pieces",'Pastel de nata']
count = 1
# for item in wish_list:
#    print(count,'-',item)
#    count += 1
list_date = [['rc car','cheerleaders','white shirts','audi r8'],['sugar laces','molten cheese','pasteis de nata','baklava']]
for num in list_date:
    counter = 1
    for data in num:
        print(counter, '-', data)
        counter += 1
