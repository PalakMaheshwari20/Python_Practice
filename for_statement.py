list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    print(num)

#printing only even numbers
for num in list1:
    if num%2==0:
        print(num)

#using else statement
for num in list1:
    if num%2==0:
        print(num)
    else:
        print('odd number')

list_sum=0
for num in list1:
    list_sum +=num
print(list_sum)

#using for loop with strings
for letter in 'This is a string':
    print(letter)

#using for loop with tuple
tup = (1,2,3,4,5)
for t in tup:
    print(t)


