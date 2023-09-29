#Lists
#A list is mutable, elements inside a list can be changed. Each element can be of different data type also
my_list = [1,2,3]
my_list = ['A string', 23, 100.32, 'o']
print(len(my_list)) #Using len() function to calculate items in a list

#concatenating string
my_list = my_list + ['new item']
print(my_list)

#duplicating list
print(my_list*2)
print("hello")
print(my_list)  #duplicating is not permanent

#Basic list methods
#append
my_list.append('append me')
print(my_list)

#pop -> By default it pop from last index, but we can also specify the index
popped_item = my_list.pop()
print(popped_item)
my_list.pop(0)
print(my_list)

#reverse
new_list = ['l','x','b','p','q']
new_list.reverse()
print(new_list)

#sort
new_list.sort()
print(new_list)

#nesting lists

lst_1 = [1,2,3]
lst_2 = [4,5,6]
lst_3 = [7,8,9]

#making list of list to form a matrix
matrix = [lst_1, lst_2, lst_3]
print(matrix)

#indexing to grab elements from matrix
print(matrix[0])
print(matrix[2][2])