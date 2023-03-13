f=open ("Menu.txt","w",encoding="utf-8") 
f.write("Please choose a pizza:\n1:Pepperoni\n2:Gennaro\n3:Hawaii\n4:Margherita\n WOULD YOU LIKE TO ADD SAUCE \n"
"5:Olives\n6:Mushrooms\n7:Bacon\n8:Corn\n9:Cheese")
f.close()
import datetime
import csv


class Pizza:
    def __init__(self,description,cost):
        self.description =description
        self.cost = cost
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
    
class Pepperoni(Pizza):
 def __init__(self):
        super().__init__("pepperoni, pepperoni sauce, mozerella cheese, corn, green olives and black olives",85)    
class Gennaro(Pizza):
  def __init__(self):
        super().__init__("mozzarella cheese, sliced sausage, marinated mushrooms, corn and thyme",74)
class Hawaii(Pizza):
  def __init__(self):
        super().__init__("pizza sauce, cheese, ham, pineapple pieces , bacon, mushrooms, peppers and sausages",85) 
class Margherita(Pizza):
  def __init__(self):
        super().__init__("tomatoes, mozzarella, basil, olive oil",100)

class Decorator(Pizza):
    def __init__(self, component,cost,description):
        self.component = component
        self.description = description
        self.cost = cost
       
    def get_description(self):
        return self.component.get_description() + ' and ' + Pizza.get_description(self)
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
   
class Olives(Decorator): 
   def __init__(self, component):
        Decorator.__init__(self,component,16,"Olives")
        
class Mushrooms(Decorator):
   def __init__(self, component):
        Decorator.__init__(self,component,12,"Mushrooms")

class Bacon(Decorator):
   def __init__(self, component):
        Decorator.__init__(self,component,30,"Bacons")

class Corn(Decorator):            
  def __init__(self, component):
        Decorator.__init__(self,component,12,"Corn")
class Cheese(Decorator):            
  def __init__(self, component):
        Decorator.__init__(self,component,17,"Cheeses")          


  
  #SİPARİŞ VERME KISMI
def main():
# Printing a menu to the screen
    with open("Menu.txt", "r",encoding = 'utf-8') as f:
        menu = f.read()
        print(menu)
    order = int(input("Please choose a pizza: "))
    while order not in [1,2,3,4]:
        order = int(input("Such an option does not exist. Please give an exist Pizza option (1,2,3,4): ")) 
    if order == 1:
        choice = Pepperoni()
    elif order == 2:
        choice = Gennaro()
    elif order == 3:
        choice = Hawaii()
    elif order == 4:
        choice = Margherita()
    else:
        print("Such an option does not exist.")
  
    bill = 0
    orderSauce = int(input("WOULD YOU LIKE TO ADD SAUCE: "))
    while orderSauce not in [5,6,7,8,9,10]:
        orderSauce = int(input("Unfortunately, it does not exist. Please give an exist Pizza option (5,6,7,8,9,10): ")) 
    if orderSauce == 5:
        description = Olives(choice).get_description()
        bill += Olives(choice).get_cost()
    elif orderSauce == 6:
        description = Mushrooms(choice).get_description()
        bill += Mushrooms(choice).get_cost()
    elif orderSauce == 7:
        description = Bacon(choice).get_description()
        bill += Bacon(choice).get_cost()
    elif orderSauce == 8:
        description = Corn(choice).get_description()
        bill += Corn(choice).get_cost()
    elif orderSauce == 9:
        description = Cheese(choice).get_description()
        bill += Cheese(choice).get_cost()
    else:
        print("Such an option does not exist.")
    print("Your Order: ",bill,"TL",description)
   
    time = datetime.datetime.now()
    date = datetime.datetime.strftime(time, '%c')
    
# Get personal information from user

    name = input("Please enter your name: ")
    idNo = input("Please enter your ID number.: ")
    cift_sayilar = ["0","2","4","6","8"]
    while len(idNo) != 11 or idNo[-1] not in cift_sayilar:
        idNo = input("Please enter a valid ID: ")

    cardNo=input("Please enter your credit card number: ")
    while len(cardNo) != 16:
        cardNo = input("Please enter a valid credit card number: ")

    cardPassword = input("Please enter your credit card password: ")
    while len(cardPassword) != 4:
        cardNo = input("Please enter a valid credit card password: ")
    print("\n************  Order Information ***********\n")
    data = [{'Name':name,'ID':idNo,'CardNo':cardNo,'CardPassword':cardPassword,'Order':description,'Date':date}]
    # Writing order information to the screen and transferring the information to the database
    with open("Orders_Database.csv", "a") as file:  
        writer = csv.DictWriter(file, fieldnames=['Name','ID','CardNo','CardPassword','Order','Date'])
        writer.writerows(data)
        file.close()
    with open("Orders_Database.csv", "r") as f:
        menu = f.read()
        print(menu)
        f.close()
main()



      