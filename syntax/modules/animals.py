from prey import Mouse, Bird

class Dog:
    def bark(self):
        return "woof!"

def show_info():
    dog = Dog()
    mouse = Mouse()
    bird = Bird()
    
    print(f"Dog says: {dog.bark()}")
    print(f"Mouse says: {mouse.squeak()}")
    print(f"Bird says: {bird.chirp()}")
