from collections import defaultdict
class bank:
    def __init__(self) -> None:
        self.map = defaultdict(dict)
    
    def line(self, s:str) ->None:
        string = s.split(': ')
        params = string[1].split(',')
        func = string[0][:]
        if func == 'CREATE_LOAN':
            self.create_loan(params)
        elif func == 'PAY_LOAN':
            self.pay(params)
        elif func == 'INCREASE_LOAN':
            self.increase(params)
    
    def create_loan(self,params):
        if params[0] in self.map and params[1] in self.map[params[0]]:
            self.map[params[0]][params[1]] += int(params[2])
        else:
            self.map[params[0]][params[1]] = 0
            self.map[params[0]][params[1]] += int(params[2])

    def pay(self,params):
        self.map[params[0]][params[1]] = max(0, self.map[params[0]][params[1]] - int(params[2]))
        if self.map[params[0]][params[1]] == 0:
            new_map = self.map[params[0]]
            del new_map[params[1]]

    def increase(self,params):
        self.map[params[0]][params[1]] += params[2]
            
    def cal(self):
        for keys in self.map.keys():
            x = 0
            for loans, money in self.map[keys].items():
                x += money
            print(f"{keys}: {x}")
    
b = bank()
b.line('CREATE_LOAN: acct_foobar,loan1,1000')
b.line('CREATE_LOAN: acct_foobar,loan2,2000')
b.line('PAY_LOAN: acct_foobar,loan2,1000')
b.cal()
