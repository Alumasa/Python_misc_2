# Calculate a running sum
add = 0
i = 1
while i == True:
    num = int(input("Please input any number: "))
    if num >= 0:
        add = add + num
        #print(add)
    if num < 0:
        print(add)
        break