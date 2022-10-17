"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly="", contract=[], commision=[]):
        self.name = name
        self.monthly = monthly
        self.contract = contract
        self.commision = commision

    def get_pay(self):
        pay = self.get_paystate()
        return pay[0]
    
    def calculate_pay(self):
        paystatement = []
        if self.monthly and (self.commision):
            if len(self.commision) == 2:
                pay = self.monthly +(self.commision[0] * self.commision[1])
                paystatement = [pay,"1"]
            else:
                pay = self.monthly + self.commision[0]
                paystatement = [pay,"2"]
        elif self.monthly and not(self.commision):
            pay = self.monthly
            paystatement = [pay,"3"]

        elif self.contract and (self.commision):
            if len(self.commision) == 2:
                pay = (self.contract[0]*self.contract[1]) +(self.commision[0] * self.commision[1])
                paystatement = [pay,"4"]
            else:
                pay = (self.contract[0]*self.contract[1]) + self.commision[0]
                paystatement = [pay,"5"]
        elif self.contract and not(self.commision):
            pay = self.contract[0] * self.contract[1]
            paystatement = [pay,"6"]
            
        
        return paystatement

    def get_paystate(self):
        x = self.calculate_pay()
        return x
    
    def __str__(self):
        paystate = self.get_paystate()
        if paystate[1] == "1":
            statement = (f"{self.name} works on a monthly salary of {self.monthly} and receives a commission for {self.commision[0]} contract(s) at {self.commision[1]}/contract. Their total pay is {paystate[0]}.")
        elif paystate[1] == "2":
            statement = (f"{self.name} works on a monthly salary of {self.monthly} and receives a bonus commission of{self.commision[0]}. Their total pay is {paystate[0]}.")
        elif paystate[1] == "3":
            statement = (f"{self.name} works on a monthly salary of {self.monthly}. Their total pay is {paystate[0]}.")
        elif paystate[1] == "4":
            statement = (f"{self.name} works on a contract of {self.contract[0]} hours at {self.contract[1]}/hour and receives a commission for {self.commision[0]} contract(s) at {self.commision[1]}/contract. Their total pay is {paystate[0]}.")
        elif paystate[1] == "5":
            statement = (f"{self.name} works on a monthly salary of {self.contract[0]} hours at {self.contract[1]}/hour and receives a bonus commission of{self.commision[0]}. Their total pay is {paystate[0]}.")
        elif paystate[1] == "6":
            statement = (f"{self.name} works on a contract of {self.contract[0]} hours at {self.contract[1]}/hour. Their total pay is {paystate[0]}.")
        return statement


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,[],[])
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"",[100,25],[])
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,[],[4,200])
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"",[150,25],[3,220])
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,[],[1500])
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"",[120,30],[600])
