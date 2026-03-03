# 1 topshiriq
class Person:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

obj=Person("Qodirali")
print(obj.get_name())
# 2 topshiriq
class Student:
    def __init__(self,age):
        self.__age=age

    def set_age(self,age):
        self.__age=age

    def get_age(self):
        return self.__age

oj=Student(20)
print(oj.get_age())   
oj.set_age(25)
print(oj.get_age())    
# 3 topshiriq
# 4 topshiriq
# 5 topshiriq
class Car:
    def __init__(self,model):
        self.__model=model

    def get_model(self):
        return self.__model

car=Car("Tesla")
print(car.get_model())
# 6 topshiriq
class Account:
    def __init__(self,password):
        self.__password=password

    def check_password(self,pwd):
        return self.__password==pwd

akkaunt=Account("mypassword")
print(akkaunt.check_password("mypassword"))  
# 7 topshiriq
# 8 topshiriq
# 9 topshiriq
# 10 topshiriq

class LoginSystem:
    def __init__(self, username, password):
        self.__username=username
        self.__password=password

    def login(self, u, p):
        if self.__username==u and self.__password==p:
            print("Salom Dunyo!")
        else:
            print("notogri username yoki password")

sistema=LoginSystem("admin","1234")
print(sistema.login("admin","1234"))
