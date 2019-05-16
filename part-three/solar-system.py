class System:
    def __init__(self, name):
        self.name = name
        self.bodies = []

    def __str__(self):
        return f"{self.name} System: {self.bodies}"

    def add(self, celestial_body):
        self.bodies.append(celestial_body)

    def add_multiple(self, *bodies):
        for body in bodies:
            self.add(body)

    def total_mass(self):
        total_mass = 0

        for body in self.bodies:
            total_mass += body.mass

        return total_mass


class Body:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __repr__(self):
        return f"{self.name}-{self.mass:.1f}"


class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year


class Star(Body):
    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type


class Moon(Body):
    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet


solar = System("Solar")

mercury = Planet("Mercury", 3.3, 15, 88)
venus = Planet("Venus", 3.5, 20, 90)
earth = Planet("Earth", 10, 24, 365)
mars = Planet("Mars", 6, 18, 105)

sun = Star("Sun", 12, "G2V")
sirius = Star("Sirius", 8.2, "a1v")

moon = Moon("Moon", 5, 12, earth)
phobos = Moon("Phobos", 5, 3, mars)
deimos = Moon("Deimos", 4.2, 4, mars)

solar.add(mercury)
solar.add_multiple(venus, earth, mars, sun, sirius, moon, phobos, deimos)

print(solar.bodies)  # [Mercury-3.3, Venus-3.5, Earth-10.0, Mars-6.0, Sun-12.0, Sirius-8.2, Moon-5.0, Phobos-5.0, Deimos-4.2]
print(solar.total_mass())  # 57.2
