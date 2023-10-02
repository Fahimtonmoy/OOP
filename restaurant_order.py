class restaurant:
    
    menu = {

        'burger': 5,
        'pizza': 10,
        'fries': 15,
        'hotdog': 20,
        'ice cream': 25,
        'donuts': 30,
        'cake': 35,
        'cupcake': 40,
        'pie': 45,
        'donut': 50,
        'cake': 55,
        'coke': 5,
        'pepsi': 5,
        'sprite': 5,
    }

    def __init__(self):
        self.totalprice = 0
        self.items = []
        self.name = input("Enter your name please: ")
    
    def order_item(self):
        while True:
            item = input("Enter the item you want to order: ")
            self.items.append(item)
            self.totalprice += self.menu[item] 
            print(f"would you like to order more?")
            more = input("if yes press '1'. Else press '0' for no.")
            if more == '1':
                continue
            elif more == '0':
                break
            else:
                print("please enter a valid input")

    def print_order(self):
        print("#" * 30)
        print(f"Customer name: {self.name}")
        print("Ordered item:",)
        for item in self.items:
            print(f"{item}", end= ' ')
            print("." * 10, end= ' ') 
            print(f"${self.menu[item]}")
        print(f"Total price is: ${self.totalprice}")
        print("Thank you for your order.")
