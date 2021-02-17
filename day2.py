# data structures in python

'''
list in python are what are array lists in java. 
Python does not have to have pre determined lengths for lists or even data types.
lists are indexed just like most other language start at 0. 
'''
# basic decleration 
lst = [] 
print(lst)
#appending a list 
lst.append('hello world')
lst.append(1)
print(lst)

lstToAppend = ['this', 'is', 'antother', 'list']
lst.append(lstToAppend)
print(lst)
'''
see how this adds the list as another element not the values in the list you need a differnt duction to do that
you actually don't neeed a loop to do this.
first lets remove the last item we just added.
'''
lst.pop()
lst.extend(lstToAppend)
print(lst)

'''
See how it iterated though and added the moen by one
'''

'''
nothing special has to be done to the list to make it a stack. 
You just have to use list.pop() and list.append() to remove and add to it.
pop can also be given an index to remove from a certain index.
.remove seraches the list and removes the element that matches
'''
print(lst)

lst.pop(0)
print(lst)

'''
Great now how do we know how long a list is. That is pretty important.
Unlike other languages that make you use .legth or .size python's is a funtion you put the data into rather than run the function on that data. 
'''

print(len(lst))

'''
looking at certain indexs in an array:
same thing as looking at certain indexs in a string.
basic structure lst[start:end], both are optional here.
Also first inclusive and second exclusive. 
'''

print(lst[0:3])

'''
to remove a whole section you can take 2 parts of a list 
'''

print(lst[1:2] + lst[4:])

'''
reversing a list is just lst.reverse()
'''
lst.reverse()
print(lst)

'''
python has an inbuild sorting function for lists, BUT all the data types must be the same in the list. 
you can sort in reverse as well. 
'''

lst2 = [4,2,7,8,3,6]
lst2.sort()
print(lst2)

lst2 = [4,2,7,8,3,6]
lst2.sort(reverse=True)
print(lst2)

'''
queues are simialar to stacks, but you can just use a library to speed up enqueu and deque.
this makes a special list that is optomized under the hood for appends and dequeues
'''
from collections import deque
# in this exaple we have some people wating in line 
queue = deque(['James', 'Ethan', 'Aaron'])
print(queue)
'''
queues are first in first out so when james us called to the counter he is the first to leave
note how the 'deque' being the unique datype is printed you can convert back to a normal list with casting.
python does this for any data type that is not an inbuilt data type.
'''
queue.popleft()
print(list(queue))

# adding the the end is 
queue.append('Michelle')
print(queue)
'''
note this could be done without library, but it is inoptimal from a run time perspective to do this.
Because when you remove an item from a list in python putting everything exept that item into a new shorteer list under the hood. 
This is true for removing any value from a list other popping the last item.
The library optimizes this under the hood to be faster.
'''

'''
Strings are teated internally as arrays of characters as manipulating a string is like manipulating an array.
'''

for char in 'hello world':
    print(char)

'''
Another type of list is a set.
It is a collection of items. These items are hashed when put in so that you can have O(1) look up times.
This also means that you can not have duplicates of items in sets.
similar to lists data types can be mixed.
'''

emptySet = set()
setWithStuff = {1, 2, 3, 4}
# appending a set is the same as a list

listWithStuff = [1, 2, 3, 4]

if 1 in setWithStuff:
    print(True)

if 1 in listWithStuff:
    print(True)

'''
In this case the rin time of the 1st if statement is much faster as it is O(1) rather than O(n) of the 2nd one.
This is becusae the 2nd one under the hood is individually checking if 1 is in the list while the 2nd one is using hashed values for quick turn around.
'''

