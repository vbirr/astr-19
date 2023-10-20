"""
Name: Vanessa Birrueta-Hernandez
Journal #1 - Session 3 Prompt

"""
# creates a class of a generic animal
class Animal(object):
    """docstring for Animal"""
    def __init__(self, arm_length, leg_length, tail, furry):
        super(Animal, self).__init__()
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.tail = tail
        self.furry = furry


    # describes the animal with all of its attributes
    def describe(self):
        description = "This animal has arm length of " + str(self.arm_length) +", leg length of " + str(self.leg_length)
        if (self.tail):
            description = description + " and has a tail"
            if (furry):
                description = description + " and is furry"
            else:
                description = description + ", but is not furry"
        else:
            description = description + " and has no tail"

            if (self.furry):
                description = description + ", but is furry"
            else:
                description = description + "nor is it furry"
            
        return description

# the main program that runs my other methods
def main():    
    animal = Animal(arm_length = 23.34, leg_length = 23.32, tail = False, furry = True)
    print(animal.describe())


#  run the main
if __name__== "__main__":
    main()


