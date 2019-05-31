from classes import Planet

naboo = Planet("Naboo", 30000, 8, 'Naboo')
print(f"Name is : {naboo.name}")
print(f"Radius is : {naboo.radius}")
print(f"the gravity is: {naboo.gravity}")
print(naboo.orbit())
print(naboo.commons())

print(Planet.spin('at a very high speed'))
