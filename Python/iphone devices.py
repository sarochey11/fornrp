devices = 1
while devices != -1:
    devices = int(input("Enter the number of devices: "))
    box = devices // 12
    leftover_devices = devices % 12

    containers = box // 30
    leftover_box = box % 30

    print ("The shipment is {} containers, {} box and {} devices".format(containers, box, leftover_devices))