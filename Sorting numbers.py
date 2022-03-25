def f1(func):
    def wrapper():
        print('started')
        func()
        print('ended')
    return wrapper

def f():
    print('wrapper')

f1(f)()






num_list = list()

num_1 = int(input("Input the first number: "))
num_list.append(num_1)
num_2 = int(input("Input the second number: "))
num_list.append(num_2)
num_3 = int(input("Input the third numbber: "))
num_list.append(num_3)

#num_list = list()

num_list.sort()

print(num_list)

print(num_list[0], num_list[1], num_list[2])

