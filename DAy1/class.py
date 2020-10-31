
class Apple:
    def __init__(self,ram,cpu):
        self.ram= ram
        self.cpu=cpu


    def config(self):
        print("cpu: {} and ram :{}".format(self.cpu, self.ram))




com1 =  Apple("16gb","I5")

com1.config()
