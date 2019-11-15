import re
sum=0
val=0
n = input("Enter string")

a = re.findall(r"^\w\d+|\d+",n)   #is used for find all integer form the alphanumeric
for i in n:
        if(i.isalpha()):
            sum=sum+1
            print(i,end="")
        elif(i.isnumeric()):
            val=val+1

print("",sum)
print(f"{a} ",val)