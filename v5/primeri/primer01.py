# Example 01: Encapsulation 
import random 

class Parrot:

    def __init__(self, name, species, weight, color):
        self.species = species
        self.name = name
        self.weight = weight
        self.color = color 
        self.__generate_serial_number()
        
    def sleeps(self): 
        sleep_time = random.randint(1, 60)
        
        print(f"Parrot {self.name} slept for {sleep_time} minutes.")
        return f"Parrot {self.name} slept for {sleep_time} minutes."
    
    def __generate_serial_number(self):
        self.__serial_number = random.randint(1, 100)
        
    def get_serial_number(self):
        print(f"Parrot {self.name} has serial number {self.__serial_number}")
        return self.__serial_number
    
    def set_serial_number(self, serial_number):
        self.__serial_number = serial_number
        

if __name__ == '__main__':
    parrot1 = Parrot("Polly", "Ara", 5, "blue")
    
    number = parrot1.get_serial_number()
    #print(f"Parrot {parrot1.name} has serial number {number}")
    
    return_value = parrot1.sleeps()
    print(return_value)
    
    parrot2 = Parrot("Molly", "Ara", 4, "red")  
    parrot2.get_serial_number()
    