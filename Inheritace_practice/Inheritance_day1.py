
class Inheritance_day1():

    def function1(self):
        print("calling function 1")

    def function2(self):
        print("calling function 2")

class e(Inheritance_day1):

    def fun3(self):
        print("Hellow")

class four(e):

    def funt4(self):
     print("Hellow function 4")

id= four()
id.funt4()
