from unittest import mock
import pytest
from ex3 import Machine, Cloud
from time import sleep

# initialize the Cloud Object
cl = Cloud()
cl.push_machine("a", 1)
cl.push_machine("b", 2)
b_machine = cl.get_machine("b")


# Check cloud initialization works
def test_cloud_initialization():
    assert cl.total_cost == 0, "doesnt initialize the cloud with constructor"


# Check if the machine initialization works
def test_machine_name_initialization():
    assert cl.machines[0].name == "a", "Machine doesnt initialize name well"


# Check if the machine initialization works
def test_machine_type_initialization():
    assert cl.machines[1].type == 2, "Machine doesnt initialize type well"


# Check if the get machine method returns a given machine object
def test_get_machine_from_machines():
    assert type(cl.get_machine("a")) is Machine, "Doesnt return a machine type"


# Check if the pop machine method removes a given machine
def test_pop_machine_from_machines():
    assert cl.pop_machine("a") is True, "Machine doesnt pop"


# Check if the start machine method starts the clock and changes the start_time value
def test_machine_start():
    b_machine.start_machine()
    sleep(5)
    assert b_machine.start_time is not None, "doesnt start the machine"


# Check if the stop machine method starts the clock and changes the stop_time value
def test_machine_stop():
    b_machine.stop_machine()
    assert b_machine.stop_time is not None, "machine doesnt stop well"


def test_if_price_right_for_machine_type():
    assert b_machine.get_price() == 5
