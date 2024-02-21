class Human:
    def eat(self):
        print("Humans eat")
    def work(self):
        print("Humans work a lot!!")

class Male(Human):
    pass
class Female(Human):
    pass

f1=Female()
f1.work()
m1=Male()
m1.eat()