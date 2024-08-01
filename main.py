class Atm:

    def __init__(self):
        self.balance = 0
        self.pin = ""
        self.create_pin()
        self.menu()

    def menu(self):
        user_input = int(input("""
Hello, please select an option to proceed :
1. Enter 1 to Change the Pin.
2. Enter 2 to Deposit Cash.
3. Enter 3 to Withdraw Cash.
4. Enter 4 to Check Balance.
5. Enter 5 to Exit.
"""))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.with_draw()
        elif user_input == 4:
            self.check_balance()
        else:
            print("Thank you. Have a nice day ")

    def create_pin(self):
        self.pin = input("Create your security pin : ")
        print("Pin created successfully !!!")
        self.menu()

    def deposit(self):
        check_pin = input("Enter your pin : ")
        if check_pin == self.pin:
            amount = int(input("Enter the amount to be deposited : "))
            self.balance = amount + self.balance
            print(f"Rs.{amount} amount has been deposited successfully.")
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()

    def check_balance(self):
        check_pin = input("Enter your pin : ")
        if check_pin == self.pin:
            print(f"The balance of your account is: Rs.{self.balance}")
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()

    def with_draw(self):
        check_pin = input("Enter your pin : ")
        if check_pin == self.pin:
            amount = int(input("Enter the amount your want to withdraw : "))
            self.balance = self.balance - amount
            print(f"The amount withdrawn is Rs.{amount}")
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()


sbi=Atm();