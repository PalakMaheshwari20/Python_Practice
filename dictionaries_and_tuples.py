#dictionary are defined with {} and : to signify key and value
my_dict = {'key1': 'value1', 'key2':'value2'}
print(my_dict['key2'])

#dictionaries are very flexible with data-types they can hold
my_dict = {'key1': 123, 'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])              #calling items from dictionary
print(my_dict['key3'][0])           #calling an index on that value  
print(my_dict['key3'][0].upper())   #calling methods on the value

#creating keys by assignment....starting off with an empty dictionary, we can add on to it
d = {}                  #creating a new dictionary
d['animal'] = 'Dog'     #creating new key through assignment
d['answer'] = 42
print(d)

d = {'key1': 1,'key2': 2,'key3': 3}
print(d.keys())            #method to return a list of all keys
print(d.values())          #method to grab all values 
print(d.items())           #method to return tuples of all items


######  Tuples  ######
t = (1,2,3)
print(len(t))  #checking length of tuple

#tuple unpacking ->iterating through a sequence that contains tuples, the item can actually be the tuple itself
list1 = [(2,4),(6,8),(10,12)]

for t in list1:
    print(t)

#unpacking
for (t1,t2) in list1:
    print(t1)

#dictionary unpacking
d = {'k1':1, 'k2':2, 'k3':3}
for k,v in d.items():
    print(k)
    print(v)
