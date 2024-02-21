class Human:
    def __init__(self,num_of_nose,num_of_eyes,num_of_heart):
        self.num_of_nose=1
        self.num_of_eyes=2
        self.num_of_heart=num_of_heart

    def eat(self):
        print("Human eat")
    def work(self):
        print("Humans work")

class Male(Human):

    def __init__(self, name, heart):
        super().__init__(self,1,2)
        self.name = name

    def flirt(self):
        print("Males flirt")

    def work(self):
        super().work()
        print("Male can code as well")

m1=Male('Prakhar',1)
m1.work()
print(m1.num_of_nose)
print(m1.name)
print(m1.num_of_nose)
print(m1.num_of_eyes)
print(m1.num_of_heart)