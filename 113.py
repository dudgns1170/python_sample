import random

# ㅗㅓㅠㅗㅕnjhn
class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.con = 0
        self.depost_log = []
        self.withdraw_log =[]

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.con += 1
            if self.con %5 ==0:
                self.balance = (self.balance * 1.01)
        self.depost_log.append(amount)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        self.withdraw_log.append(amount)


    def display_info(self):
        print(self.name)
        print(self.account_number)
        print(self.bank)
        print(format(self.balance,","))

    def deposit_history(self):
        for amount in self.depost_log:
            print(amount)
        #print(self.depost_log.append(self.deposit))


    def withdraw_history(self):
        print(self.withdraw_log.append(self.withdraw))




K = Account("kim", 10000)
L= Account("Lim",100000)
P= Account("park",1200000)
K.deposit(1000)
K.withdraw(2000)
K.deposit(13000)
K.withdraw(3000)
K.deposit_history()
K.withdraw_history()
print(K.balance)


lists = []
lists.append(K)
lists.append(L)
lists.append(P)

for i in  range(len(lists)):
    if lists[i].balance >= 1000000:
        lists[i].display_info()





