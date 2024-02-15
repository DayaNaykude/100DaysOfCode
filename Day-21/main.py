class Animal:
    def __init__(self, animal_type):
        self.no_of_eyes = 2
        self.animal_type = animal_type

    def breath(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self, animal_type, dangerous):
        super().__init__(animal_type)
        self.is_dangerous = dangerous

    def breath(self):
        super().breath()
        print("doing in underwater")


animal = Animal("wild")
print(animal.animal_type)

fish = Fish("marine",True)

print(fish.animal_type)
fish.breath()

