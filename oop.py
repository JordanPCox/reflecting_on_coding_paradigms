class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

        def repair(self):
            self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"



#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
#It demonstrates encapsulation by bundling attributes and methods into a class. It demonstrates inheritance with the AnakinsPod and SebulbasPod classes using super to inherit methods of the parent Podracer class. It demonstrates polymorphism with the repair method in the Podracer class, and flame_jet in the SebulbasPod class. Abstraction is not explicitly demonstrated here.

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#No, it would go against DRY principles by requiring you to repeat a lot of code, whereas with OOP we can uses classes to pass data.

#How in particular did Object Oriented Programming assist in the solving of this problem?
#Using the parent Podracer parent class is useful by allowing AnakinsPod and SebulbasPod to inherit its attributes and methods, ensuring consistency and increasing efficiency.