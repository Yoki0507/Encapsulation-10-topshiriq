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
class User:
    def __init__(self,age):
        self.__age=age

    def get_age(self):
        return self.__age

    def setter(self):
        if self.__age>0:
            return f"Notogri"
        else:
            return f"Togri"

data=int(input("Yoshingizni kiriting: "))
user=User(data)
print(user.setter())
# 4 topshiriq
class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.__balance=balance 

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Yetarli mablag yoq!")

obj=BankAccount("Qodirali",1500000)
print("Balans:",obj.get_balance())
obj.deposit(50000)
obj.withdraw(900000)
print("Oxirgi balans:",obj.get_balance())
# 5 topshiriq
class Car:
    def __init__(self,model):
        self.__model=model

    def get_model(self):
        return self.__model

car=Car("Ferrari")
print(car.get_model())
# 6 topshiriq
class Account:
    def __init__(self,password):
        self.__password=password

    def parol(self,pwd):
        return self.__password==pwd

akkaunt=Account("mypassword")
print(akkaunt.parol("mypassword"))  
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

sistema=LoginSystem("Qodirali","0705")
print(sistema.login("Qodirali","0705"))
