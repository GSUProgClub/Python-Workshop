# PH Python workshop demo file - type this out as you go

# Obligatory Hello World and how prints work
print('hello world')

# Assinging variables and basic data types
# Strings
a = 'hello world 2'
print(a)

one, two = 3, 4

print(one)
print(two)
'''
numbers are diffent in python 
when assiging a number it is always a float by default
if you want an int to be calculated you have to do something differnt.
either you alwasys use whole numbers, cast a float to an int or use floors
'''

intExample = 1
floatExample = 1.1

'''
check point question:
will the following code error T/F?
'''
floatExample =  intExample - floatExample
print(floatExample)


'''
Another thing you can do in python is you can re assing any variable at anypoint
b/c of how it runs top to bottom and is an interperated language.
Warn: This can lead to type mismatches if not careful
'''

a = 204
print(a)

'''
checkpoint question:
will the following code give trailing 3s?
'''
print(4/3)

#Floor division - This is interger divison in other languages. b/c by default in python everything is floats
print(4 // 3)

# Mod - find the remainder
b = 10
print(a % b)
print(4 % 3)

'''
checkpoint question:
calcualte the volume of the prism:
length: 4
width: 3
height: 2
'''

# Logic - how python assinges booleans
a = 24
b = 72
boolFlag = True
boolFlag2 = False
'''
if statements and how they work
mention how python uses tabs and white space to determin what cobe belongs to what block
for simple if statemtns you can use no () but for more complex or layered if statments () wil lbe needed
! is not in many alngeues ain pyton it is just 'not'
&& is and in many langues in pyton it is just 'and'
| is or in many langues in python is is just 'or'
>, <, >=, <=, ==, and != are the same as other languages
'''

if boolFlag and boolFlag2:
    print(a)
else:
    print(b)

if boolFlag or boolFlag2:
    print(a)
else:
    print(b)

if (boolFlag or boolFlag2) and not boolFlag2:
    if not (a >= b):
        print(a)
else:
    print(b)


'''
loops
They work different than other langueages. 
Alot of uselful improvements other other langues while keeping it simple
'''
# java style while loop
i = 0
while i <= 20:
    print(i)
    i += 1

j = 0
arr = [1, 2, 3, 4, 5]
while j <  5:
    print(arr[j])
    j += 1

# the python way of doing it - this does not allow for element manipulation
for item in arr:
    print(item)

# sum of 0 to 10
total = 0
for i in range(11):
    total += i
print(total)

'''
range is pyton's way of quickly generating an enumerated list for loops
range is first inclusive and last esclusive
range can also take a stepping value as a 3rd value
range(start, stop, step)
1 is the default value of step
''' 

x = range(10)
print(x)
for val in x:
    print(val)

# num_lst = range(11)
# print(sum(num_lst))
total = sum(range(11))
print(total)