string = str(input('enter a string: '))
length = len(string)
if length >3:
    if string[-3: ] != 'ing':
        print(string + 'ing')
    else:
        print(string + 'ily')
else:
    print('the string is only of three letters')
