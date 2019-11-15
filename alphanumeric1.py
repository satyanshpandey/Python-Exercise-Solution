sum1 = ""
sum2 = 0
x = input("Enter Alphanumeric number")
# a = re.findall(r"[^\w\d_]+|\d+","23psq23a")   #is used for find all integer form the alphanumeric
# a = re.findall(r"[^\d_]+|\d",x)     #this method is used for find all integers form the alphanumeric
print(x)
for i in x:
    try:
        if(i.isalpha()):
            if (sum2==0):
                    sum2=1
            sum1=sum1+(sum2*i.upper())
            sum2=0
        else:
                sum2=int(str(sum2)+str(i))
    except:
        pass
print(f"The Format in which you want to print is :{sum1}")
input()