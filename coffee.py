class Machine:
    def __init__(self):
        self.money, self.water, self.milk, self.beans, self.cups = 550, 400, 540, 120, 9

    def print_state(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money""")

    def buy(self):
        e_water, e_beans, e_money = 250, 16, 4
        l_water, l_milk, l_beans, l_money = 350, 75, 20, 7
        c_water, c_milk, c_beans, c_money = 200, 100, 12, 6
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        option = (input())
        if option == "1":
            if self.water >= e_water and self.beans >= e_beans:
                print("I have enough resources, making you a coffee!")
                self.money += e_money
                self.beans -= e_beans
                self.water -= e_water
                self.cups -= 1
            elif self.water < e_water:
                print("Sorry, not enough water!")
            else:
                print("Sorry, not enough beans!")
        elif option == "2":
            if self.water >= l_water and self.beans >= l_beans and self.milk >= l_milk:
                print("I have enough resources, making you a coffee!")
                self.money += l_money
                self.milk -= l_milk
                self.water -= l_water
                self.beans -= l_beans
                self.cups -= 1
            elif self.water < l_water:
                print("Sorry, not enough water!")
            elif self.milk < l_milk:
                print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough beans!")

        elif option == "back":
            self.run_program()
        else:
            if self.water >= c_water and self.beans >= c_beans and self.milk >= c_milk:
                print("I have enough resources, making you a coffee!")
                self.money += c_money
                self.milk -= c_milk
                self.water -= c_water
                self.beans -= c_beans
                self.cups -= 1
            elif self.water < c_water:
                print("Sorry, not enough water!")
            elif self.milk < c_milk:
                print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough beans!")


    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input())
        print("Write how many ml of milk you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.beans += int(input())
        print("Write how many disposable coffee cups you want to add:")
        self.cups += int(input())

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def do_smth(self, action):

        if action == "buy":
            return self.buy()
        elif action == "take":
            return self.take()
        elif action == "remaining":
            self.print_state()
        else:
            return self.fill()

    def run_program(self):

        while True:
            print("\nWrite action (buy, fill, take, remaining, exit):")
            do = input()
            if do != "exit":
                coffee.do_smth(do)
            else:
                exit()


coffee = Machine()
coffee.run_program()


