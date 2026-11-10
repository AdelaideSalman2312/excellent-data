class Lamp:
    def __init__(self):
        self.on = False

    def switch(self):
        self.on = not self.on
        return self.on

lamp = Lamp()
print(lamp.switch(), lamp.switch()) 