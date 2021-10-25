class Country:
    def __init__(self, name:str, population:int, area:float):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self,other_country):
        if (self.area > other_country.area):
            return True
        else:
            return False

    def population_density(self):
        return self.population/self.area
    
    def __str__(self):
        return '{} has a population of {} and is {} square km.'.format(self.name, self.population, self.area)

    def __repr__(self):
        return "Country('{0}', {1}, {2})".format(self.name, self.population, self.area)
canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)

print(canada.name)
print(canada.population)
print(canada.area)

if (canada.is_larger(usa) == True):
    print("Canada is larger than USA")
else:
    print("Canada is not larger than USA")

print(canada.population_density())
print(usa.population_density())

print([canada])
print(canada)