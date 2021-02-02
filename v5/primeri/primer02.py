# Example 02: Abstraction 
import random 

class Cage:
    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.parrots = []
        
    def fly_in(self, parrot):  
        self.parrots.append(parrot)


class Parrot:

    def __init__(self, name, species, weight, color):
        self.species = species
        self.name = name
        self.weight = weight
        self.color = color 
        self.__generate_serial_number()
              
    def fly(self):
        in_cage = random.randint(0, 1)
        if in_cage == 1:
            cage.fly_in(self)
            self.cage = cage 
            print(f"Parrot {self.name} is in cage {self.cage.name}")
        else:
            print(f"Parrot {self.name} is flying free!")
    
    def sleeps(self): 
        sleep_time = random.randint(1, 60)
        
        print(f"Parrot {self.name} slept for {sleep_time} minutes.")
        return f"Parrot {self.name} slept for {sleep_time} minutes."
    
    def __generate_serial_number(self):
        self.__serial_number = random.randint(1, 100)
        
    def get_serial_number(self):
        print(f"Parrot {self.name} has serial number {self.__serial_number}")
        return self.__serial_number
        

if __name__ == '__main__':
    cage = Cage("Cage 1", 10)
    parrot1 = Parrot("Polly", "Ara", 5, "blue")
    
    parrot1.fly()
    parrot1.get_serial_number()
    parrot1.sleeps()
    
    print(f"Number of birds in cage {cage.name} : {len(cage.parrots)}")
    
    parrot2 = Parrot("Molly", "Ara", 4, "red")  
    parrot2.fly()
    parrot2.get_serial_number()
    
    print(f"Number of birds in cage {cage.name} : {len(cage.parrots)}")
    