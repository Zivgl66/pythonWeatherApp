import random

barrles = 1500
poisoned = random.randint(0,1500)

def find_poisoned_barrel(poisoned):
    slaves = {"1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "11":1, "11":1}
    for slave in slaves:
        step = 2 ** (int(slave) -1)
        # print(f'step: {step}')
        for num in range(int(slave),barrles, step):
            print(num)
            if num == poisoned:
                slaves[slave] = 0
    slaves_list = list(slaves.values())
    slaves_list.reverse()
    print(slaves_list)
    number = ''.join(str(x) for x in slaves_list)
    print(f'poisoned barrel is: {poisoned}')
    print(int(number,2))
    
find_poisoned_barrel(poisoned)
            
    
    