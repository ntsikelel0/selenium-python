class Demo(object):

    num = 100

    def __init__(self, a, b):
        print("This is a constructor and is called automatically, when an object is created")
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def multiply(self):
        return self.num1 * self.num2

    def subtract(self):
        return self.num1 - self.num2

    def divide(self):
        return self.num1 / self.num2

    def remainder(self):
        return self.num1 % self.num2


obj = Demo(2, 3)
print(obj.add())
print(obj.multiply())
print(obj.subtract())
print(obj.divide())
print(obj.remainder())