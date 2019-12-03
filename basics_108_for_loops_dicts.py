#continuing for loops
#this time for dictionaries
dict_data ={1:{'name':'Bronson','money': 0.50},
            2:{'name':'Janet','money': 3.50},
            3:{'name':'Bartholomew','money': 5.50},
            4:{'name':'Vanessa','money': 7.50}
            }
#when you do a simple for loop on a dictionary you get the individual keys
# for key in dict_data:
#     #if you want to get the value of the key use dict[key]
#     print(dict_data[key])
#     #for vals in key:
#        # print(vals)
#     print(type(key))
# for key in dict_data:
#     print(key,'-->',dict_data[key])
#we want the name of the person
#and how much they owe us..
#after we apply the interest (%4000)
for key in dict_data:
    print(dict_data[key]['name'], 'owes us:',dict_data[key]['money']*(4000/12))
