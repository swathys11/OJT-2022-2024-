import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def validate_age(self):
        try:
            age = int(self.age)
            if age < 0:
                return False
            return True
        except ValueError:
            return False
    
    def validate_email(self):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, self.email) is not None
    
    def is_valid(self):
        return self.validate_age() and self.validate_email()

if __name__ == "__main__":
    person1 = Person("John", 25, "john@example.com")
    if person1.is_valid():
        print("Person is valid.")
    else:
        print("Person is not valid.")
    person2 = Person("Alice", -30, "alice@")
    if person2.is_valid():
        print("Person is valid.")
    else:
        print("Person is not valid.")
