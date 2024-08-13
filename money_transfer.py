# /***
#  * At Stripe we keep track of where the money is and move money between bank accounts to make sure their balances are not below some threshold.
#  * This is for operational and regulatory reasons, e.g. we should have enough funds to pay out to our users, and we are legally required to separate our users' funds from our own.
#  * This interview question is a simplified version of a real-world problem we have here.
#  * Let's say there are at most 500 bank accounts, some of their balances are above 100 and some are below.
#  * How do you move money between them so that they all have at least 100?
#  * Just to be clear we are not looking for the optimal solution, but a working one.
#  *
#  * Example input:
#  * - AU: 80
#  * - US: 140
#  * - MX: 110
#  * - SG: 120
#  * - FR: 70
#  * Output:
#  * - from: US, to: AU, amount: 20
#  * - from: US, to: FR, amount: 20
#  * - from: MX, to: FR, amount: 10
#  *
#  * followup1：反过来问，假设给你一系列transfer，问最后account balance是否满足条件。假设所给account balance无论如何也无法做到每个account>=100，问所给的transfer是不是best effort？
#  * followup2：如何得到最优解？这里你需要问面试官如何定义最优解。面试官说转账次数越少越好。这样和LC0465就很像了
#  */
from collections import defaultdict
# class Bank:
#     def __init__(self) -> None:
#         self.data = list()

#     def add_string(self,s:str) -> None:
#         bank_details = s.split(': ')
#         self.data.append(([bank_details[0]],int(bank_details[1])))

#     def transactions(self):
#         output = list() #from // to // amount
#         self.data.sort(key = lambda x : x[1])
#         l = 0
#         r = len(self.data)-1
#         while l<r and self.data[l][1]<100:
#             if self.data[r][1]>100:
#                 amount = max(self.data[r][1] - 100, 100 - self.data[l][1])
#                 self.data[l][1] += amount
#                 self.data[r][1] -= amount
#                 output.append(self.data[r][0],self.data[l][0],amount)
#                 if self.data[l][1] > 100:
#                     l += 1
#             else:
#                 r -= 1
        
#         for items in self.data:
#             if items[1] <100 : 
#                 print('something is wrong')
#                 break
#         else: 
#             self.printit(output)
        
#     def printit(self,output:list):
#         for item in output:
#             print(f"from {item[0]} to {item[1]} : {item[2]}")
    
        
# b = Bank()
# b.add_string('AU: 80')
# b.add_string('US: 140')
# b.add_string('MX: 110')
# b.add_string('SG: 120')
# b.add_string('FR: 70')

# b.transactions()

class Bank:
    def __init__(self) -> None:
        self.data = list()

    def add_string(self, s: str) -> None:
        bank_details = s.split(': ')
        self.data.append([bank_details[0], int(bank_details[1])])

    def transactions(self):
        output = list()  # from // to // amount
        self.data.sort(key=lambda x: x[1])  # Sort accounts by balance
        l = 0
        r = len(self.data) - 1

        while l < r and self.data[l][1] < 100:
            if self.data[r][1] > 100:
                amount = min(self.data[r][1] - 100, 100 - self.data[l][1])
                self.data[l][1] += amount
                self.data[r][1] -= amount
                output.append((self.data[r][0], self.data[l][0], amount))

                if self.data[l][1] >= 100:
                    l += 1
                if self.data[r][1] == 100:
                    r -= 1
            else:
                r -= 1

        for items in self.data:
            if items[1] < 100:
                print('Something is wrong: Balance less than 100')
                break
        else:
            self.printit(output)

    def printit(self, output: list):
        for item in output:
            print(f"from {item[0]} to {item[1]} : {item[2]}")

b = Bank()
b.add_string('AU: 100')
b.add_string('US: 100')
b.add_string('MX: 110')
b.add_string('SG: 120')
b.add_string('FR: 70')

b.transactions()
