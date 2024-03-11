import datetime
import time
from functools import reduce

'''
This is a Python Module that has 2 Classes. Machine class for creating a new machine, parameters are name and ype of 
machine (1 or 2). Cloud class, which is a list that holds all machines and lets you get separate price of each machine 
and price of all used machines.
'''


class Machine:
    # machine constructor (name and type)
    def __init__(self, name, machine_type):
        self.name = name
        self.type = machine_type
        self.start_time = None
        self.stop_time = None

    # get price of machine
    def get_price(self):
        if self.type == 1:
            return 2
        return 5

    # Boot a machine using time library to get today's time.
    def start_machine(self):
        if self.start_time is not None:
            return
        else:
            self.start_time = datetime.datetime.now()
            self.stop_time = None

    # Shut down a machine and hold the time
    def stop_machine(self):
        self.stop_time = datetime.datetime.now()

    # calculate the cost of a machines run time
    def calculate_cost(self):
        if self.start_time:
            if self.stop_time:
                return ((self.stop_time - self.start_time).total_seconds() // 60.0) * self.get_price()
            return ((datetime.datetime.now() - self.start_time).total_seconds() // 60.0) * self.get_price()
        return "Machine has not started"


class Cloud:
    machines = []

    # Constructor to hold total price of all machines
    def __init__(self):
        self.total_cost = 0

    # Add a machine, create it and add it to the machines list
    def push_machine(self, name, machine_type):
        for machine in self.machines:
            if name == machine.name:
                print("Machine already exists")
                return
        new_machine = Machine(name, machine_type)
        self.machines.append(new_machine)

    # Remove a machine from the machines list
    def pop_machine(self, machine):
        if len(self.machines) == 0:
            return "No machines in the cloud"
        for i in range(len(self.machines)):
            if self.machines[i].name == machine:
                self.machines.pop(i)
                return True

    # Get a specific machines object using its name
    def get_machine(self, machine):
        if len(self.machines) == 0:
            return "No machines in the cloud"
        for i in range(len(self.machines)):
            if self.machines[i].name == machine:
                return self.machines[i]

    # Get separate price for each machine at this given time
    def get_separate_prices(self):
        if len(self.machines) != 0:
            for i in self.machines:
                print(f"Machine {i.name} price at the moment: {i.calculate_cost()}$")
            return
        return 1

    # Calculate the price of all machines in the list at the moment.
    def calculate_price_of_all(self):
        if len(self.machines) != 0:
            sum_of = 0
            for i in self.machines:
                sum_of += i.calculate_cost()
            return sum_of
        return 0

    # Print all machines in the machines list (name and type)
    def get_all_machines(self):
        if len(self.machines) != 0:
            for i in self.machines:
                print(f"Machine {i.name} of type: {i.type}")

# cl = Cloud()
# cl.push_machine("a", 1)
# cl.push_machine("b", 1)
# cl.push_machine("c", 1)
# cl.push_machine("d", 2)
# cl.push_machine("e", 2)
# cl.get_all_machines()
# # cl.pop_machine("a")
# # cl.get_all_machines()
# # print(cl.get_machine("a").type)
#
# cl.get_machine("a").start_machine()
# cl.get_machine("b").start_machine()
# cl.get_machine("c").start_machine()
# cl.get_machine("d").start_machine()
# cl.get_machine("e").start_machine()
#
# date_str = "2024-03-07 17:58:34"
# e_date_str = "2024-03-07 17:59:34"
# date_stop = "2024-03-07 18:00:34"
# date_stop1 = "2024-03-07 18:01:34"
# dt_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
# e_dt_obj = datetime.datetime.strptime(e_date_str, '%Y-%m-%d %H:%M:%S')
# dt_obj_stop = datetime.datetime.strptime(date_stop, '%Y-%m-%d %H:%M:%S')
# dt_obj_stop1 = datetime.datetime.strptime(date_stop1, '%Y-%m-%d %H:%M:%S')
#
# cl.get_machine("a").start_time = dt_obj
# cl.get_machine("b").start_time = dt_obj
# cl.get_machine("c").start_time = dt_obj
# cl.get_machine("d").start_time = dt_obj
# cl.get_machine("e").start_time = e_dt_obj
#
# cl.get_machine("b").stop_time = dt_obj_stop
# cl.get_machine("a").stop_time = dt_obj_stop1
# cl.get_machine("d").stop_time = dt_obj_stop1
# cl.get_machine("c").stop_time = dt_obj_stop1
# cl.get_machine("e").stop_time = dt_obj_stop1
# cl.get_separate_prices()
# print(f"price of all machines is: {cl.calculate_price_of_all()}$")
