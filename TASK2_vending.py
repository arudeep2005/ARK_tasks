class VendingMachine:
    def __init__(self):
        self.juices = {
            "PEPS": {"name": "Pepsi", "price": 30, "quantity": 50},
            "MDEW": {"name": "Mountain Dew", "price": 30, "quantity": 50},
            "DPEP": {"name": "Dr. Pepper", "price": 50, "quantity": 50},
            "COKE": {"name": "Coke", "price": 20, "quantity": 50},
            "GATO": {"name": "Gatorade", "price": 20, "quantity": 50},
            "DCOK": {"name": "Diet Coke", "price": 30, "quantity": 50},
            "MINM": {"name": "Minute Maid", "price": 25, "quantity": 50},
            "TROP": {"name": "Tropicana", "price": 30, "quantity": 50}
        }
        self.current_state = self.your_choice

    def your_choice(self):
        print("Available drinks:\n")
        for code, juice in self.juices.items():
            print(f"{juice['name']} - {code} (${juice['price']})")
        print("\n")
        choice = input("Enter the drink code: ").upper()
        if choice in self.juices:
            self.selected_drink = self.juices[choice]
            if self.selected_drink["quantity"]<=0:
                print("Enter another choice as all cans of this choice are used")
                self.current_state=self.your_choice
            else: self.current_state = self.money_process
            
        elif choice == "REFILL":
            self.refill_juices()
        else:
            print("Drink code is wrong. Please try again.")

    def money_process(self):
        amount = int(input("Enter the amount of money: "))
        if amount < self.selected_drink["price"]:
            print("Not enough money. Please enter a sufficient amount.\n")
        else:
            change = amount - self.selected_drink["price"]
            self.cans_process()
            print(f"Here's your change: ${change}\n")
            self.current_state = self.your_choice

    def cans_process(self):
        self.selected_drink["quantity"] -= 1
        print(f"\nEnjoy your {self.selected_drink['name']}!")

    def refill_juices(self):
        for code, juice in self.juices.items():
            juice["quantity"] = 50
        print("Juices have been refilled.\n")

    def run(self):
        while True:
            self.current_state()

m = VendingMachine()
print("\nWelcome to the vending machine!\n")
m.run()
