#TIME MODULE FULL CONCEPT AND USES:----


# # Full concept of date and time module
import datetime
def gatedate():
    return datetime.datetime.now()
t = gatedate()
print(t)
y = str([t.date()])
print(y)

print("This is t",t)

print("The date is",y)
y = y.split("-")

print("The date is:::====>",y)
y = y[::-1]
print("after split functio")
s = t.day
d = t.date()
print("Today's day is",s)
a = t.month
print("now MONTH IS",a)
n = t.year
print("Todays year",n)

print("Today's DATE is",d)
          #This is the use of Split method in python
text = 'Hello satyansh bhai please add 1 and 5 '
print(text)
print(text.split("-"))








# import time
# k=0
#
# initial=time.time()# is use for calculate the execution time of the While loop
# while( k<3):
#         print("satyansh is a good boy")
#         k+=1
# print("While Loop in ran",initial)
#
# initial2=time.time()# is use for calculate the execution time of the for loop
# for i in range(3):
#     print("Satyansh is a good boy")
#
#     time.sleep(1)#This function is use for delay of the Execution of the program!
#
# print("for Loop in ran",initial2)
#
# localtime=time.asctime(time.localtime(time.time()))# This Function is use for find the Time with Exact Date and Day
# print("Today's time=>",localtime)
# #     time.sleep(1)#This function is use for delay of the Execution of the program!
#
#
# print("My name is satyansh pandey \r Hello friends my name is satyansh pandey")#'\r' is use for skeep before sentence\
