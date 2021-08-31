num=int(input("enter your number"))
sum = 0
temp = num
while(temp>0):
    digit = temp %10
    sum +=  digit **3
    temp //= 10

if sum == num:
    print("given number is amstrong number")
else:
    print('given number is not an amstrong number')


