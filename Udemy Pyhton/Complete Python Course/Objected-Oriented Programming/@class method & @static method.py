

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
    # cls stands for class, not object


myObject = Foo()
myObject.hi()


class Bar:
    @staticmethod
    def hi():
        print("Hello, I don\'t take parameters.")


anotherObject = Bar()
anotherObject.hi()


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    # fixed decimal number

    @staticmethod
    def fromSum(value1, value2):
        return FixedFloat(value1 + value2)
    # if inherited, it will still show the method as it created

    @classmethod
    def fromSum1(cls, value1, value2):
        return cls(value1 + value2)
    # if inherited, it does not matter, cls will call the subclass
    # use class method, never use static method


number = FixedFloat(18.5746)
newNumber1 = number.fromSum(19.575, 0.789)
newNumber2 = FixedFloat.fromSum(19.575, 0.789)
print(number)
print(newNumber1)
print(newNumber2)


class Euro(FixedFloat):
    def __int__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f'<Euro ${self.amount:.2f}>'


money = Euro(18.786)
money1 = Euro.fromSum(16.758, 9.999)
money2 = Euro.fromSum(16.758, 9.999)
money3 = Euro.fromSum1(16.758, 9.999)
print(money)
print(money1)
print(money2)
print(money3)


