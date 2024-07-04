# Encapsulation
# Encapsulation refers to restricting access. This is how we can wrap up and remove unnecessary data. So basically, Encapsulation is the process of using private variables within classes to prevent unintentional modification of data.

class myClass(object):
    def __init__(self):
        self.a = 123  # public variable
        self._b = 123  # protected variable
        self.__c = 123  # private variable, double underscore

obj = myClass()
print(obj.a)  # accessible, public variable
print(obj._b)  # accessible, protected variable
print(obj.__c)  # not accessible, will raise an AttributeError

# Private variables are intended to be changed using getter and setter methods. These provide indirect access to them.
class myClass(object):
    def __init__(self):
        self.__version = 22  # private variable, double underscore

    def getVersion(self):
        print(self.__version)

    def setVersion(self, version):
        self.__version = version

obj = myClass()
obj.getVersion()  # This will print 22
obj.setVersion(23)
obj.getVersion()  # This will print 23

# Accessing the private variable directly will result in an AttributeError
# print(obj.__version)  # Uncommenting this line will raise an AttributeError

# Accessing the mangled private variable
print(obj._myClass__version)  # This will print 23

