
doors = []
x = 1
for x in range(1, 101):
    doors.append({'door': x, 'state': 'closed'})
    x += 1
    i = 1

def toggledoors(doors, i):

    for var in doors:

        if var['door'] in range(0, 101, i):
            if var['state'] == "closed":
                var['state'] = "open"
            else:
                var['state'] = "closed"


while i in range(1, 101):
    toggledoors(doors, i)
    i += 1

print("########## Door states ##########")
for var in doors:
    if var['door'] in range(0, 101):
        if var['state'] == "open":
            print(var['door'], ', ', var['state'])


