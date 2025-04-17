class Pet:
    def __init__(self, name="bobby") #< --fixed __init__ method
        self.name = name
        self.hunger = 4
        self.energy = 7
        self.happiness = 8
        self.tricks = []

        def eat(self):
            self.hunger = max(0, self.hunger -3)
            self.happiness = min(10, self.happiness  +1)

        def sleep(self):
            self.energy = min(10, self.energy +5)3
        
        def play(self):
            self.energy = max(0, self.energy -2)
            self.happiness = min(10, self.happpiness +2)
            self.hunger = min(10, self.hunger +1)

        def get_status(self):
            print(f"name:{self.name}")
            print(f"hunger:{self.hunger}")
            print(f"energy:{self.energy}")
            print(f"happiness:{self.happiness}")

        def train(self, trick):
            self.tricks.append(trick)

        def show_tricks(self):
            print(f"{self.name} knows the following trick: {', '.join(self.tricks)}")

        #create an instance of the Pet class
        pet = Pet("Fluffy")

        #call the methods to test them
        pet.get_status()
        pet.eat()
        pet.sleep()
        pet.play()
        pet.train("roll over")
        pet.train("open doors")
        pet.show_tricks()
