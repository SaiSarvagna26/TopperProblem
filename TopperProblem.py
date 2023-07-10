n=int(input())
str_n=str(n)
even=0
odd=0
for i in str_n:
    if int(i)%2==0:
        even+=int(i)
    else:
        odd+=int(i)
if even==odd:
    print("true")
else:
    print("false")