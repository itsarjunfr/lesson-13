row = int(input('Rows: '))
x=0
for i in range(row):
    for j in range(i+1):
        x=x+1
        print(x, end=(' '))
    print()