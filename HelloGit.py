# comment
print("Hello, World!")
a =6
b= 5
print(a + b)


# how to make a list
mylist = [1,2,3,4,3,2,1]

#how to stride
print(mylist[0:6:2])# from index 0 to 6, skip 2

#strings are just lists
phrase = 'Catch the dog'
phrase[2]# t
phrase[4] # h
phrase[-1:0:-3] #strides work backwards, -1 is right, 0 is left, down by 3

# how to acces elements of a list
print(mylist[1])

#how to write a function
def sumFunction(a, b):
	return a + b

#how to call a function
print(sumFunction(2,20))

x = 10
y = -10

# blocks of code
if(x == 10):
	x = 5
elif(y == -10):
	y = 5
else:
	x = y - x

#loop
mylist = [1,3,8,412,43,2,20]

#length of list
len(mylist)

#while
x = 0
y = 0
while(x<5)
        y+2
        x+1
#for loop by index
for i in range(len(mylist)):
	print(mylist[i])

#for each loop
for val in mylist:
	print(val)

#dictionaries
lookup ={}
lookup['kc'] = 'chiefs'
lookup['ne'] = 'patriots'
lookup['la'] = 'chargers'
lookup['suck'] = 'raiders'
