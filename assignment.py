class Bank(object):
    def __init__(self,BankId=int,BankName=str,Location=str,Tellers=3,Customers=10,Banks=2):
        self.BankId = BankId
        self.BankName = BankName
        self.Location = Location
        self.Tellers = {}
        self.Customers = {}
        self._Banks = Banks

class  Customer(Bank):
    def __init__(self,CustomerId=int,CustomerName=str,Address=str,PhoneNo=int,AccountNo=int):
        self.CustomerId = CustomerId
        self.CustomerName = CustomerName
        self.Address = Address
        self.PhoneNo = PhoneNo
        self.AccountNo = AccountNo
    def General_incquiry(self):
        print('how can we be of help?')
    def DepositMoney(self):
        pass
    def WithdrawMoney(self):
        pass
    def OpenAccount(self):
        self.CustomerName= input('First name:                                    ' ,'Last name:                        ')
        self.Address = input('Address: ')
        self.PhoneNo = input('Phone No: ')
        self.CustomerId = self.CustomerId
        self.AccountType = input('Savings/Checking:')

        self.AccountNo = self.AccountNo
    def CloseAccount(self):
        pass
    def Apply_for_loan(self):
        pass
    def Request_for_Card(self,CustomerName):
        self.CustomerName = CustomerName
        print('We are working on it!')

class Teller(Customer,Bank):
    def __init__(self,TellerId=int,TellerName=str):
        self.TellerId = TellerId
        self.TellerName = TellerName
    def CollectMoney(self):
        pass
    def OpenAccount(self):
        pass
    def CloseAccount(self,CustomerId):
        if CustomerId == CustomerId:
            del self.CustomerId
        else:
            print('Null Id')
    def LoanRequest(self):
        pass
    def ProvideInfo(self):
        print('How can I help?')
    def IssueCard(self):
        print('Be patient with us!')
class Account(Teller,Customer,Bank):
    def __init__(self,CustomerName,AccountId=int, Balance=0.00):
        self.CustomerName = CustomerName
        self.Balance = Balance
    def DepositMoney(self,Amount):
        self.Balance +=Amount
    def WithdrawMoney(self,Amount):
        if Amount > self.Balance:
            raise
        ValueError('Insufficient Funds')
        self.Balance -=Amount
    def get_Balance(self):
        return self.Balance
class SavingsAccount(Account):
    def __init__(self, CustomerId,AccountId):
        super(self,SavingsAccount).__init__(self)
        self.AccountId = AccountId
        self.CustomerId = self.CustomerId
class CheckingAccount(Account):
    def __init__(self, CustomerId,AccountId):
        super(SavingsAccount,self).__init__(self)
        self.AccountId = AccountId
        self.CustomerId = self.CustomerId
class Loan():
    def __init__(self,CustomerId,AccountId,LoanId=int,LoanType=str):
        self.LoanId = LoanId
        self.LoanType = LoanType
        self.AccountId = self.AccountId
        self.CustomerId = self.CustmerId
    def Request_for_Loan(self,Name,LoanId,LoanType,amount=float):
        self.Name=input('Name:')
        self.LoanId=LoanId
        self.LoanType=LoanType
        self.amount=amount

Bank1=Bank(10001,'Bank1','Kampala')
z1 = {
    'Teller01':1001,
    'Teller02':1002,
    'Teller03':1003

}
Bank1.Tellers.update(z1)
print(Bank1.Tellers)
r={
    'CustomerId':101,'CustomerName':'james','Address':'seta','PhoneNo':777,'AccountNo':111,
'CustomerId':102,'CustomerName': 'joe', 'Address': 'set', 'PhoneNo': 788, 'AccountNo': 112,
'CustomerId':103,'CustomerName': 'jona', 'Address': 'sat', 'PhoneNo':827, 'AccountNo': 113,
'CustomerId':104,'CustomerName': 'jones', 'Address': 'sada', 'PhoneNo': 987, 'AccountNo': 114,
'CustomerId':105, 'CustomerName': 'jas', 'Address': 'soroti', 'PhoneNo': 907, 'AccountNo': 115,
'CustomerId':106, 'CustomerName': 'jack', 'Address': 'sent', 'PhoneNo': 897, 'AccountNo': 116,
'CustomerId':107, 'CustomerName': 'sam', 'Address': 'pata', 'PhoneNo': 867, 'AccountNo': 117,
'CustomerId':108, 'CustomerName': 'him', 'Address': 'seroma', 'PhoneNo': 457, 'AccountNo': 118,
'CustomerId':109,'CustomerName': 'jeans', 'Address': 'sironko', 'PhoneNo': 767, 'AccountNo': 119,
'CustomerId':110,'CustomerName': 'jacs', 'Address': 'sheta', 'PhoneNo': 778, 'AccountNo': 120
}
Bank1.Customers.update(r)
print(Bank1.Customers)
Bank2=Bank(10002,'Bank2','Moroto')
z2 = {
    'Teller01':1012,
    'Teller02':1022,
    'Teller03':1033

}
Bank2.Tellers.update(z2)
print(Bank2.Tellers)
r1={
    'CustomerId':1001,'CustomerName':'james','Address':'seta','PhoneNo':9777,'AccountNo':111,
'CustomerId':2002, 'CustomerName': 'joe', 'Address': 'set', 'PhoneNo': 80788, 'AccountNo': 112,
'CustomerId':2003, 'CustomerName': 'jona', 'Address': 'sat', 'PhoneNo': 827, 'AccountNo': 113,
'CustomerId':2004, 'CustomerName': 'jones', 'Address': 'sada', 'PhoneNo': 9987, 'AccountNo': 114,
'CustomerId':3005, 'CustomerName': 'jas', 'Address': 'soroti', 'PhoneNo': 9907, 'AccountNo': 115,
'CustomerId':6006, 'CustomerName': 'jack', 'Address': 'sent', 'PhoneNo': 7897, 'AccountNo': 116,
'CustomerId':3007, 'CustomerName': 'sam', 'Address': 'pata', 'PhoneNo':60867, 'AccountNo': 117,
'CustomerId':2008, 'CustomerName': 'him', 'Address': 'seroma', 'PhoneNo': 8457, 'AccountNo': 118,
'CustomerId':1009, 'CustomerName': 'jeans', 'Address': 'sironko', 'PhoneNo': 5767, 'AccountNo': 119,
'CustomerId':100, 'CustomerName': 'jacs', 'Address': 'sheta', 'PhoneNo': 8778, 'AccountNo': 120,
}
Bank2.Customers.update(r1)

print(Bank2.Customers)

Bank1=Bank( )
