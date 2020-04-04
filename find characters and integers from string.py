sum=0
strval=""
val=0
intval=""
n = input("Enter string")
try:
    for i in n:
            if(i.isalpha()):
                sum=sum+1
                strval=strval+i
            elif(i.isnumeric()):
                val=val+1
                intval=intval+i
            else:
                pass
except:
    pass
print(f"{strval} have {sum} char")
print(f"[{intval}]   {val} ")
