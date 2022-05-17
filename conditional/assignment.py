print("Computer Bazar: ")
print("1. dell(Rs.20000)  2. Toshiba(Rs.30000)  3. Mac(Rs.50000)")
print("Select the model of computer")
option=int(input("Enter the option number: "))

quantity=int(input("Enter the quantity: "))

print("Enter the option of delivery: ")
print(" 1. home(Rs. 1000)  2. Pickup(free) ")
delivery=int(input("Enter the option number: "))

print("Enter the option of packaging: ")
print(" 1. plastic(Rs.500)  2. Bag (Rs.1000)  3. Gift box(Rs.5000)  4. None")
packaging=int(input("Enter the option number: "))


print("Enter the location : ")
print(" 1. Ktm (13% tax)  2. ltp (free)  3. bkt (free)")
location=int(input("Enter the option number: "))



if option==1:
    total1=20000
elif option==2:
    total1=30000
else:
    total1=50000

total2=total1*quantity

if delivery==1:
    total3= total2+1000
else:
    total3=total2

if packaging==1:
    total4=total3+500
elif packaging==2:
    total4=total3+1000
elif packaging == 3:
    total4 = total3 + 5000
else:
    total4=total3

if location==1:
    total5=total4+(0.13*total1)
else:
    total5=total4

print(f"The total price of the customer is: {total5}")