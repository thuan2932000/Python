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

    
class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        total = 0
        for country in self.countries:
            total = total + country.population
        return total

    def __str__(self):
        res = self.name
        for country in self.countries:
            res = res + '\n' + str(country)
        return res       

canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040,9826675)
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)
print(north_america.name)
for country in north_america.countries:
    print(country)
print(north_america.total_population())
print(north_america)