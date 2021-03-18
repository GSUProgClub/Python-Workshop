'''
object oriented python
'''

'''
What is object oriented programming?
-it is structuring you programming so that you are budling related properties and behaviors into objects
-this won't be a OOP toutorial, but a OOP in python tutorial

note to self make all this some powerpoint slides later


first some keywords:

class 
- this is how you define a class in python
- like in other languages class is the 'blueprint' you use to build an object
- angain like in other languages an instance of an object means that the blueprint has been used to make an object and you are using it
- this keyword is followed by the name of the class then a ':' similar to how in other languages you use {}

__init__()
- this is what in other languages is the constuctor method

self
- this the same as using 'this' in java
- every method in an object's class has to have this as the first parameter
- when you call it you don't use self, you use it when you make the class 
- this included the __init__() too

__str__
- this is how you over ride the string fuction of the object
- without this when you go to print your object it would output the memeory adress of the object
- this is effivly overriding the same as '.toSring()' in java

__add__
- this how you over ride the '+' of python so you can esily add to object without makeing a differnt method


now lets move to a new file that we will called 'monster.py'
'''