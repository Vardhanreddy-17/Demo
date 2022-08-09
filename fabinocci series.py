print("Enter the how many terms required:")
a=int(input())
b=0
c=1
count=0
if a < 0:
    print("Enter a positive value")
elif a == 0:
    print(b)
elif a == 1:
    print(c)
else:
    while count<=a:
        d=b+c
        print(b)
        b=c
        c=d
        count = count + 1
