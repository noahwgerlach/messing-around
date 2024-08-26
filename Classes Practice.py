class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
country = Country("Iceland", "Reykjavik")

print(country.name)
print(country.capital)