class Fish:
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species

        self.alive = True

    def bye_bye(self):
        self.alive = False

    def __repr__(self):
        if self.alive:
            eye = "o"
        else:
            eye = "*"
        return f"><((({eye}>"


class MegaFish(Fish):
    def __init__(self, name, color, species):
        super().__init__(name, color, species)
        self.lives = 10

    def bye_bye(self):
        self.lives -= 1
        if self.lives == 0:
            self.alive = False

    def eat(self, fish):
        print(f"yum, I ate {fish.name}")
        fish.bye_bye()
        print(f"{fish.name} is {fish}")


if __name__ == "__main__":
    pet = Fish("jimmy", "blue", "goldfish")
    print(pet.name)
    print(pet)

    print()

    mega_pet = MegaFish("REEE", "rainbow", "swordfish")
    print(mega_pet.name)
    print(mega_pet)

    mega_pet.eat(pet)
