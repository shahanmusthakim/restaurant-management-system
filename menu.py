class Menu:
    def __init__(self):
        self.items=[]
        
    def add_menu(self,name):
        self.items.append(name)
        
    def find_item(self,name):
        for itm in self.items:
            if itm.name.lower()==name.lower():
                return itm
        return None
    
    def remove_item(self,name):
        item=self.find_item(name)
        if item:
            self.items.remove(item)
            print(f'{name} removed.\n')
            
        else:
            print(f'{name} not found') 
        
    def view_menu(self):
        print("\n-------------VIEW MENU-------------\n")
        print("NAME\tPRICE\tQUANTITY")
        for itm in self.items:
            print(f'{itm.name}\t{itm.price}\t{itm.quantity}')