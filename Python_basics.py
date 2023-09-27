#STRING BASICS

#Printing a string
print('Hello to the python world')
a = "Hello World"
print(type(a))

#To check the length of a string!
n = len(a)
print("Length of String a is : ", n)

#String indexing

print(a[0])
print(a[1])

#Performing string slicing
print(a[1:])    # Grabs everything after the first term all the way to length of string
print(a)        # There is still no change in original string
print(a[:3])    # Grabs everything upto 3rd index---->here is does not include 3rd index
print(a[:])     # Everything
print(a[-1])    # Last letter(One index behind 0 so it loops back around)
print(a[:-1])   # Grabs everything except the last letter

# we can use two colons in a row and then a number specifying the frequency to grab elements
print(a[::1])   # Grabs everything, but go in size of 1
print(a[::2])   # Grabs everything, but go in size of 2
print(a[::-1])  # We use this to print string backwards
#a[0] ='p'
#print(a)    #Results in error due to property that string is immutable

# Concatenation of string
a = a + ' concatenate me'
print(a)

#Using multiplication symbol for repetition
letter = 'z'
print(letter*10)

#Basic built-in string methods
print(a.upper())    #Upper case a string
print(a.lower())    #lower case a string
print(a.split())    #split a string by blank space(this is default)
print(a.split('o'))    #split a string by a specific element(does not include the element that was split on)


