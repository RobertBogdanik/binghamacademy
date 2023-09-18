class Fan:
    def __init__(self, speed = 1, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def getSpeed(self):
        return self.__speed

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def getOn(self):
        return self.__on

    def setSpeed(self, speed):
        self.__speed = speed

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def setOn(self, on):
        self.__on = on

    def __str__(self):
        return "Speed: " + str(self.__speed) + "\nColor: " + self.__color + "\nRadius: " + str(self.__radius)+ "\nOn: " + str(self.__on)

fan1 = Fan(3, 10, "yellow", True)
fan2 = Fan(2, 5, "blue", False)

print(fan1)
print(fan2)
