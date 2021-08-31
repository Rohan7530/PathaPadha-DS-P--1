sum1 = 0
sum2 = 0
for i in range (21, 30):
    if i % 2 ==0:
        sum1+= i
    else:
        continue

for i in range (21, 30):
    if i % 2 ==1:
        sum2+= i
    else:
        continue

print('sum of even numbersare',sum1)
print('sum of odd numbers are',sum2)



