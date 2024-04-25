def airport(take_off, landing):
    take_off = dict((x,take_off.count(x)) for x in set(take_off))
    landing = dict((x,landing.count(x)) for x in set(landing))
    for key, value in take_off.items():
        if (landing[key] + value) % 2 != 0:
            return key
    return "Airport is empty"
    

print(airport([1234, 2345, 3456, 4567, 1234,1234], [2345, 1234, 3456, 4567, 1234])) 

def airport2(list_of_planes):
    list_of_planes = dict((x,list_of_planes.count(x)) for x in set(list_of_planes))
    for key, value in list_of_planes.items():
        if value % 2 != 0:
            return key
    return "Airport is empty"

print(airport2([1234,1234,2345,3456,2345]))

    