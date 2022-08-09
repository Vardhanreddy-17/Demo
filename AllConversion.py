
def listtodic(a):
    output = {stu: "RANK" for stu in a}
    return output
def listtotupler(a):
    output=tuple(a)
    return output
def tupletolist(b):
    output=list(b)
    return output
def tupletodic(b):
    output={t:"RANKK" for t in b}
    return output
a=[1,2,3,4]
b=(1,2,3,4,5)
output1=listtodic(a)
output2=listtotupler(a)
output3=tupletolist(b)
output4=tupletodic(b)
print(output1)
print(output2)
print(output3)
print(output4)