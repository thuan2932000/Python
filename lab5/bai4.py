class Nematode:
    def __init__(self, length:int, gender:str, age:int):
        self.length = length
        self.gender = gender
        self.age = age
    def str(self):
        return 'Nematode: {}mm long, gender is {}, {} days old'.format(self.length, self.gender, self.age)
    def repr(self):
        return "Nematode({}, '{}', {})".format(self.length, self.gender, self.age)
worm = Nematode(1.1, 'hermaphrodite', 2)
print(worm.length)
print(worm.gender)
print(worm.age)
print(worm.str())
print(worm.repr())