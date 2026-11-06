from menu import Menu
class Restaurent:
    def __init__(self,name):
        self.name=name
        self.emploees=[]
        self.menu=Menu()
        
        
    def add_employee(self,emplyoee):
        self.emploees.append(emplyoee)
        
    def view_employee(self):
        print("\n-------EMPLOYEE LIST-------\n")
        for e in self.emploees:
            print(e.name,e.email,e.phone,e.address,e.designation,e.salary)