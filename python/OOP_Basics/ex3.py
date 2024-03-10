import datetime
import time
from functools import reduce


class Machine:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.start_time = None
        self.stop_time = None

    def get_price(self):
        if self.type == 1:
            return 2
        return 5

    def start_machine(self):
        if self.start_time:
            return
        else:
            self.start_time = datetime.datetime.now()

    def stop_machine(self):
        self.stop_time = datetime.datetime.now()

    def calculate_cost(self):
        if self.start_time:
            if self.stop_time:
                return ((self.stop_time - self.start_time).total_seconds() // 60.0) * self.get_price()
            return ((datetime.datetime.now() - self.start_time).total_seconds() // 60.0) * self.get_price()
        return


def calculate(*argv):
    return reduce(lambda x, y: int(x) + int(y), argv)


class Cloud:
    machines = []

    def __int__(self):
        self.total_cost = None

    def push_machine(self, name, type):
        new_machine = Machine(name, type)
        self.machines.append(new_machine)

    def pop_machine(self, machine):
        if len(self.machines) == 0:
            return
        for i in range(len(self.machines)):
            if self.machines[i].name == machine:
                self.machines.pop(i)
                return

    def get_machine(self, machine):
        if len(self.machines) == 0:
            return
        for i in range(len(self.machines)):
            if self.machines[i].name == machine:
                return self.machines[i]

    def get_separate_prices(self):
        if len(self.machines) != 0:
            for i in self.machines:
                print(f"Machine {i.name} price at the moment: {i.calculate_cost()}")
            return
        return 1

    def calculate_price_of_all(self):
        if len(self.machines) != 0:
            sum_of = 0
            for i in self.machines:
                sum_of += i.calculate_cost()
            return sum_of
        return 0

    def get_all_machines(self):
        if len(self.machines) != 0:
            for i in self.machines:
                print(f"Machine {i.name} of type: {i.type}")


cl = Cloud()
cl.push_machine("a", 1)
cl.push_machine("b", 1)
cl.push_machine("c", 1)
cl.push_machine("d", 2)
cl.push_machine("e", 2)
cl.get_all_machines()
# cl.pop_machine("a")
# cl.get_all_machines()
# print(cl.get_machine("a").type)

cl.get_machine("a").start_machine()
cl.get_machine("b").start_machine()
cl.get_machine("c").start_machine()
cl.get_machine("d").start_machine()
cl.get_machine("e").start_machine()

date_str = "2024-03-07 17:58:34"
e_date_str = "2024-03-07 17:59:34"
date_stop = "2024-03-07 18:00:34"
date_stop1 = "2024-03-07 18:01:34"
dt_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
e_dt_obj = datetime.datetime.strptime(e_date_str, '%Y-%m-%d %H:%M:%S')
dt_obj_stop = datetime.datetime.strptime(date_stop, '%Y-%m-%d %H:%M:%S')
dt_obj_stop1 = datetime.datetime.strptime(date_stop1, '%Y-%m-%d %H:%M:%S')

cl.get_machine("a").start_time = dt_obj
cl.get_machine("b").start_time = dt_obj
cl.get_machine("c").start_time = dt_obj
cl.get_machine("d").start_time = dt_obj
cl.get_machine("e").start_time = e_dt_obj

cl.get_machine("b").stop_time = dt_obj_stop
cl.get_machine("a").stop_time = dt_obj_stop1
cl.get_machine("d").stop_time = dt_obj_stop1
cl.get_machine("c").stop_time = dt_obj_stop1
cl.get_machine("e").stop_time = dt_obj_stop1
cl.get_separate_prices()
print(f"price of all machines is: {cl.calculate_price_of_all()}$")
print(cl.machines)
