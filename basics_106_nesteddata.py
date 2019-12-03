#Nested data in lists and dictionaries
mix_list =['strings',98,['more string',[1,2,4,7]]]
#print(type(mix_list[2]))
internal_list = mix_list[2]
#print(internal_list)
#print(internal_list[1][2])
#embedded dictionaries
embedded_dict = {'status': 'operational','key1':['car keys','boat keys','mansion keys','dog house keys'],
'staff': {'Julius Ceasar':{'name' : 'Julio','last_name' : 'Cesar','birth_date':1979,'football club':'flamengo'},
'Julia Venus':{'name':'Julia','last_name':'venus','birth_date':1969,'football club':'CubaFC'}}}
#print:
#the boat keys and dog house keys
##inside the key 'staff, print the dictionary with the key 'Julio Cesar'
##From the dict with the key Julia Venuss,print:
### last name,birth date and the football'
print(embedded_dict['key1'][1])
print(embedded_dict['key1'][3])
print(embedded_dict['staff']['Julius Ceasar'])
print(embedded_dict['staff']['Julia Venus']['last_name'])
print(embedded_dict['staff']['Julia Venus']['birth_date'])
print(embedded_dict['staff']['Julia Venus']['football club'])

# #for i in embedded_dict:
#     for j in i:
#      if j == 'Julius Ceasar':
#         print('Julius Ceasar')
#         j = +1
#      for [k] in j:
#          if k == 'last_name' or 'birth_date' or 'football club':
#              print('last_name','birth_date','football club')
#      else:
#         break
#
