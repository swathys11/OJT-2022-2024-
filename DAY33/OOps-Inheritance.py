
# Inheritance
# By using inheritance, we can create a class that uses all the properties and behavior of another class. In Inheritance we have a parent and a child class, as in real life a child inherits the characteristics of his/her parents, likewise, child class has properties of the parent class.

class Flower:
    def color(self):
        print("Flowers are found in various colors")

    def scientific_name(self):
        print("These are some Binomial nomenclature for categorize species")

    def family(self):
        print("Every flower has a family")

    def odour(self):
        print("Every flower has its own odour by which it can be identified")

class Jasmine(Flower):
    def color(self):
        print("Jasmine flower comes in white, pink, blue, orange, yellow, purple, and red color")

    def scientific_name(self):
        print("Jasminum sambac is the scientific name of Jasmine")

    def family(self):
        print("Jasmine is from the Oleaceae family")

class Lily(Flower):
    def color(self):
        print("Lilies commonly grow in white, yellow, pink, red, and orange color.")

    def scientific_name(self):
        print("Lilium is the scientific name of Lily")

    def family(self):
        print("Lily is from the Liliaceae family")

obj_Flower = Flower()
obj_jasmine = Jasmine()
obj_lily = Lily()

obj_Flower.color()
obj_Flower.scientific_name()
obj_Flower.family()
obj_Flower.odour()

obj_jasmine.color()
obj_jasmine.scientific_name()
obj_jasmine.family()
obj_jasmine.odour()

obj_lily.color()
obj_lily.scientific_name()
obj_lily.family()
obj_lily.odour()
