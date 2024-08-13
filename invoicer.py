from collections import defaultdict
class Invoice:
    def __init__(self, timestamp, name, amount):
        self.timestamp = timestamp
        self.name = name
        self.amount = amount

class Invoicer:
    def __init__(self):
        self.sendSchedule = {
            -10: "Upcoming",
            0: "New",
            20: "Reminder",
            30: "Due"
        }
        self.invoices = defaultdict(Invoice)

    def add_invoice(self, timestamp, name, amount):
        self.invoices[timestamp] = Invoice(timestamp, name, amount)

    def output(self):
        res = []
        message_list = []
        
        for timestamp in self.invoices:
            for time_delta in self.sendSchedule:
                scheduled_time = timestamp + time_delta
                message_list.append((scheduled_time,f'[{self.sendSchedule[time_delta]}] Invoice for {self.invoices[timestamp].name} for money'))

        message_list.sort(key=lambda m: m[0])
        
        for message in message_list:
            res.append(f'{str(message[0])}: {message[1]}')
        
        return res

# Test run
def run():
    sol = Invoicer()
    sol.add_invoice(0, "Alice", 200)
    sol.add_invoice(1, "Bob", 100)
    output = sol.output()
    for message in output:
        print(message)

run()

