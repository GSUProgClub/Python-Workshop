'''
first lets make make the class
you can have the class and the code running the class in one file or you can use muliple files 
if you make one big file just make the classes at the top
if you you multiple files use imports
here we will use one big file 
'''

class person:
    
    # 1. now we can define the constuctor
    def __init__(self, name, age):
        # in java you would have to define the instance variables first, but in python you do not have so

        self.name = name
        self.age = age

    # 3. self HAS to be used where ever you do anything with the object since that is how python knows which instance to manipulate
    # 3. similar to how java uses 'this'
    def __str__(self):
        # this return uses a thing called a f string that is python 3.6+ that allows you to 
        return f'{self.name} is {self.age}'

    # 4. lets give out person to say a getter for later
    def say(self):
        return 'hello there'

    def getAge(self):
        return self.age

# 6. lets make another class to show polymorphism
class dog:
    def __init__(self, name, age, owner, breed):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = breed

    def __str__(self):
        return f'{self.name} is {self.age} years old, is owned by {self.owner}, and is a {self.breed}'
    
    def say(self):
        return 'woof'
    
    def getAge(self):
        return self.age
#2. 
greg = person('Greg', 23)
#2. see there we didn't define the __str__ in the class so it prints out the memory adress
print(greg)
#3. lets go back and add it 

# 4. 
print(greg.say())

# 7. 

dogMike = dog('Mike', 2, greg, 'Husky')

print(dogMike)
print(dogMike.say())
print()

# 8. polymorphism example

dog1 = dog('good boy 1', 2, greg, 'Husky')
dog2 = dog('good boy 2', 4, greg, 'Husky')
dog3 = dog('good boy 2', 1, greg, 'Husky')

person1 = person('person 1', 23)
person2 = person('person 2', 35)
person3 = person('person 3', 20)

mixedLst = [dog1, person1, dog2, person2, dog3, person3]

'''
What is the expected output?
- error or use say method
'''
for item in mixedLst:
    print(item.say())