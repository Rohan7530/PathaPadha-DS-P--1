string = str(input('enetr your string'))
size = len(string)

if size >=2:
    firstTwoChar = string[0:2]
    lastTwochar = string[-2:]
    answer = firstTwoChar + lastTwochar
    print(answer)

else:
    print('empty string')