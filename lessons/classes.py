class Planet():

    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape}'

    @staticmethod
    def spin(speed='200 minse per hour'):
        return f'The planets spins and spins at {speed}'


hoth = Planet("Hoth", 20000, 5.5, 'Hoth System')

print(f"Name is : {hoth.name}")
print(f"Radius is : {hoth.radius}")
print(f"the gravity is: {hoth.gravity}")
print(hoth.orbit())

naboo = Planet("Naboo", 30000, 8, 'Naboo')
print(f"Name is : {naboo.name}")
print(f"Radius is : {naboo.radius}")
print(f"the gravity is: {naboo.gravity}")
print(naboo.orbit())
print(naboo.commons())

print(Planet.spin('at a very high speed'))
