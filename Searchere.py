import re
txt="Python is one of the most popoular language"
searchobj=re.search("\s",txt)
print("The first white-space character is located",searchobj)