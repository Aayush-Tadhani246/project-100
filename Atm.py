class Atm:
    def __init__(self,pin,cardNumber):
        self.cardnumber = cardNumber
        self.pin = pin

    def check_balance(self):
        balance = 100000000
        print("Your balance is " + balance)

    def withdrawl(self,amount):
        updated_amount = 1000000000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(updated_amount))


def main():
    Card_number = input("insert your card number ")
    Pin_number  = input("enter your pin number ")

    new_user =  Atm(Card_number,Pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number"))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount "))
        new_user.withdrawl(amount)

if __name__ == "__main__":
    main()
