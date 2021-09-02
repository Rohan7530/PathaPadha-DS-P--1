stg = str(input('enter a string'))
size = len(stg)
if ( size >= 2):
    first2 = stg[0 : 2]
    last2  = stg[-2:]
    output = first2 + last2
    print(output)
else :
    print("empty string")