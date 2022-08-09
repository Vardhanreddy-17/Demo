import re
txt = "Use of python in machine Learning"
x=re.search("^Use.*Learning$",txt)
if(x):
    print("Yes! We have a match!")
else:
    print("No match")