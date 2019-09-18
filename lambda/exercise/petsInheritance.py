# Create a Pets class that holds instances of dogs; 
# this class is completely separate from the Dog class. In other words, the Dog class does not 
# inherit from the Pets class. Then assign three dog instances to an instance of the Pets class.
#  Start with the following code below. Save the file as pets_class.py. Your output should 
#  look like this:I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they're all mammals, of course.

# Parent class
class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

class Pets(Dog):
    super.__init__()

