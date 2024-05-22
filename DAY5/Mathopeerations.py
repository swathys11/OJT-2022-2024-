#Create a class called MathOperations with class methods for basic mathematical operations 
# like addition, subtraction, multiplication, and a static method to find the factorial of a number.


class MathOperations:
    @classmethod
    def addition(cls, num1, num2):
        return num1 + num2

    @classmethod
    def subtraction(cls, num1, num2):
        return num1 - num2

    @classmethod
    def multiplication(cls, num1, num2):
        return num1 * num2

    @staticmethod
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * MathOperations.factorial(num - 1)
if __name__ == "__main__":
    print("Addition:", MathOperations.addition(5, 3))
    print("Subtraction:", MathOperations.subtraction(5, 3))
    print("Multiplication:", MathOperations.multiplication(5, 3))
    print("Factorial:", MathOperations.factorial(5))
