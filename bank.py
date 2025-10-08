class bank:
    def __init__(self,name,balance,pin):
        self.name=name
        self.balance=balance
        self.pin=pin
        self._is_active = True
        self._atm_requested = False
        self._cheque_requested = False
        print(f"Account created for {self._name} with balance ₹{self._balance}")
    def check_pin(self,userpin):
        return userpin==self.pin
    def check_balance(self,userpin):
        if not self._is_active:
            print("account is frozen")
            return
        if not self.check_pin(userpin):
            print("invalid pin")
            return
        print(f' your ammount {self.balance}')
    def withdraw(self,balance):
    
        amount = int(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
    def deposit(self,balance):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print(f"your total balance is :{self.balance}")
    def atmrequest(self):
        if  self._atm_requested:
            print("alredy reuest")
        else:
            self._atm_requested=True
            print("your rwquest is approvel ")
    def check_balance(self):
        if self._cheque_requested:
            print("already requested")
        else:
            self._cheque_requested=True
            print("Approve request")
    def accountfrezze(self):
        if self._is_active:
            print("Freeze account")
        else:
            self._is_active=False
            print("account already frozen")
    def accountunfrezze(self):
        if self._is_active :
            print("account already active")
        else:
            self._is_active=True
            print("Unfreeze account.")


        
            



class savingaccount(bank):
    def __init__(self, name, balance, pin,intalbalance):
        super().__init__(name, balance, pin)
        self.intalbalance=intalbalance
        def withdraw(self,name,pin):
            pass

class bussinessaccount(bank):
    pass







        