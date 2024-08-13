from collections import defaultdict
import string

def next_server_number(current_numbers):
    '''Function to allocate new server numbers.'''
    if not current_numbers:
        return 1
    else:
        highest_number = max(current_numbers)
        for num in range(1, highest_number):
            if num not in current_numbers:
                return num
        return highest_number + 1

class Tracker:
    def __init__(self):
        self.host_types = defaultdict(list)   #noice to know this very hard 
    
    def allocate(self, host_type):
        '''Function to allocate new server numbers.'''
        available = next_server_number(self.host_types[host_type])
        self.host_types[host_type].append(available)
        return '{}{}'.format(host_type, available)
    
    def deallocate(self, hostname):
        '''Function to deallocate the inputted server.'''
        # Find the position where the numeric part starts
        last_letter = 0
        for i, char in enumerate(hostname):
            if char.isdigit():
                last_letter = i - 1
                break
        
        host_type = hostname[:last_letter + 1]
        host_num = int(hostname[last_letter + 1:])
        
        if host_num in self.host_types[host_type]:
            self.host_types[host_type].remove(host_num)
        return None

# Example Usage:
tracker = Tracker()
print(tracker.allocate("apibox"))    # "apibox1"
print(tracker.allocate("apibox"))    # "apibox2"
print(tracker.deallocate("apibox1")) # None, deallocates "apibox1"
print(tracker.allocate("apibox"))    # "apibox1", reuses "apibox1"
print(tracker.allocate("sitebox"))   # "sitebox1"

