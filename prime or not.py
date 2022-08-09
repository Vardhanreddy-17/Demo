print("enter the number:")
a=int(input())
count = 0
for i in range(1,a):
    if(a%i==0):
      count += 1

if(count<=1):
    print("IT IS A PRIME NUMBER")
else:
    print("IT IS NOT PRIME NUMBER")


 