"""
class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model
car = Car("Audi", "04")
print(car)

Enhance this class such that when we print the object itself sprint(car),
it prints in the following format ("Company": "Audi", "Model": "04")
"""

class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def __str__(self):
        return f'{{"Company": "{self.company}", "Model": "{self.model}"}}'

car = Car("Audi", "04")
print(car)

