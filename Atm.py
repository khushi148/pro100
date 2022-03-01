class Atm():
    def __init__(self,card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def CashWithDrawl(self):
        print("your money is withdrawed")

    def BalanceEnquiry(self):
        print(" your balance is $ 10,000")

    def cardNo(self,card_number):
        print("your card number is : "+ card_number)

withd=Atm(200,500)
print(withd.CashWithDrawl())
print(withd.BalanceEnquiry())
print(withd.cardNo("200"))

