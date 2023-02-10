CURRENT_YEAR = 2022
METER_TO_FEET = 3.2808

a=input("Your Firstname")
b=input("Your Lastname")
year_born= int(input("when were you born: "))
height_meter = float(input("Your height (meter): "))
is_male = input("Are your male (yes/no): ")

age = CURRENT_YEAR - year_born
height_feet= height_meter*METER_TO_FEET
height_feet= round(height_feet,1)

if is_male =="yes" :
	is_male = True
elif is_male == "no":
	is_male = False
else:
	is_male= None

print("-----")
print("your name is "+a+" "+b)
print("Your age: "+ str(age))
print("Your Height (feet): "+ str(height_feet))