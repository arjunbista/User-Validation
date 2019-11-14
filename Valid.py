import sys
name=input("Enter your Name: ")
for x in range(1,4):
    if name.isalpha()==True and len(name)>=3:
        print("Valid Name")

        break
    else:
        print("Invalid name")
        name = input('enter name again')
print("Please follow next step")
age=input("Enter your Age: ")
for y in range(1,3):
    if age.isdecimal()==True and int(age)>=18:
        print("Valid age")
        break
    else:
        print("Invalid age details")
        age=input("Re Enter your age: ")
mob=input("Enter your Mobile number: ")
for z in range(1,3):
    if mob.isdigit()==True and len(mob)==10:
        print("Valid Mobile Number")
        break
    else:
        print("INVALID Mobile number")
        mob=input("Re Enter your mobile: ")
sys.exit("Please follow next Time")


