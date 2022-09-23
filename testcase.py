class car():
    def __init__(self, name ,transmission):
        self.name = name
        self.transmission = transmission
    def show_object_details(self):
        print("The Object details:")
        print("The name is ",self.name)
        print("The trasnmission is:",self.transmission)

a = input("Enter the name:")
b = input ("Enter the trasnmission:")

audi = car(a,b)

#showing the object details
audi.show_object_details()
