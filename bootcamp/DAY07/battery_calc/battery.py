def battery(battery,time):
    while battery > 1 :
        battery = battery*2/3
        time += battery * 1.2
    time += 120
    return time
print(battery(100,120))
