def prime():
    n1 = int(input("enter the number for CheckingThePrimeNumber1:"))
    n2 = int(input("enter the number for CheckingThePrimeNumber2:"))
    for num in range(n1,n2+1):
        if num>1:
          for i in range(2,num) :
              if num%i==0:
                  break
          else:
              n = num
              print(num)

# (Help)
# print(n)  "Can we not print the value of the num as assign in variable(n)...?"


def Leap():
    print("Enter the year for checking leap year")
    num = int(input("Enter:"))
    if num % 4 == 0 or num % 400 == 0:
        print("The number you entered is LeapYear:")
    else:
        print("IS not LeapYear:")

# print(prime())
# n = prime()
# print(n)

# try:
#     prime()
#     print(num)
# except:
#     print("")head=35
# leg=94
# number_of_rabbit=(leg-2*head)/2
# if(number_of_rabbit==int(number_of_rabbit)):
#     number_of_chicken = (4 * head - leg) / 2
#     print(f"You have {int(number_of_chicken)} chickens and {int(number_of_rabbit)} rabbits.")
#
# else:
#     print("Sorry from the given heads and legs we are not able to calculate....Solution not possible")