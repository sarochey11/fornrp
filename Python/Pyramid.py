blocks =int(input("Enter the number of blocks: "))


remaining = blocks
height = 0
used = 0
#num = 1
while remaining > 0:
    if remaining > height:
        height += 1
    used = used + height
    remaining -= height
    print('remaining: ', remaining, ' used: ', used, 'sum: ', remaining + used)

print("The height of the pyramid: ", height)