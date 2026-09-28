def show_fruits(fruit):  # Parameterized function
    print(f"my favorite fruit is: {fruit}")

pf=2000 #global scope variable

show_fruits("orange") # argument passed to the function


def calculate_salary(basic_salary, hra, da, bonus):  # Parameterized function
    #pf=basic_salary * 0.12 #local scope variable
    print(f"Provident Fund: {pf}")  # This will raise an error because pf is not defined in this scope)
    total_salary = (basic_salary + hra + da + bonus) - pf
    return total_salary

def calculate_attendance(attendance, total_days):
    attendance_percentage = (attendance / total_days) * 100
    return attendance_percentage

bonus = 5000
working_days = 22
total_days = 30
attendance_percentage = calculate_attendance(working_days, total_days)  # arguments passed to the function
print(f"Attendance percentage: {attendance_percentage}%")

if(attendance_percentage > 70):
 bonus = 10000
else:
 bonus = 0

wages_per_day = 1000
extra_wages_per_day=0
# day=6 # 1 Monday,6,7 Sat Sund

# match day:
#    case 1 | 2|3 |4 |5:
#       print("Monday")

#    case 6 | 7:
#        extra_wages_per_day=2000

#print(extra_wages_per_day)


#While loop

#monday saundy 1 t0 7

#day 6 or 7 extra wages add kart hai
# day=1
# while day <= 7:
#     if day == 6:
#         extra_wages_per_day += 2000
#         print(f"Extra wages per day: {extra_wages_per_day}")
#     day += 1 #2


    

# #calling the function with arguments
# basic_salary = (working_days * wages_per_day)+extra_wages_per_day
# print(f"basic salary: {basic_salary}")
# hra = 10000 
# da = 5000


# salary = calculate_salary(basic_salary, hra, da, bonus)  # arguments passed to the function
# print(f"Total salary: {salary}")

# print(f"Provident Fund: {pf}")  # This will raise an error because pf is not defined in this scope)






# 30 days in a month
# 1 first gold rate 20000
# 2 21000
# 30 22000

# har dina 1k incremnt in gold rate

# totale end of 30 th day 


# for loop to calculate gold rate for 30 days
starting_rate = 20000
daily_increment = 1000
days = 30

for day in range(1, days + 1):
    rate = starting_rate + (day - 1) * daily_increment
    print(f"Day {day}: ₹{rate}")

print("30th Day Gold Rate:", rate)


# while loop to calculate total gold rate for 30 days

gold_rate = 20000
day = 1
total = 0

while day <= 30:
    print(f"Day {day}: ₹{gold_rate}")
    
    total = total + gold_rate
    gold_rate = gold_rate + 1000
    day = day + 1

print(f"\nTotal for 30 days: ₹{total}")






# #print(pf)  # This will raise an error because pf is not defined in this scope)
# salary = calculate_salary(50000, 10000, 5000, 5000)  # arguments passed to the function
# print(f"Total salary: {salary}")

# salary = calculate_salary(60000, 10000, 5000, 5000, 2000)  # arguments passed to the function
# print(f"Total salary: {salary}")


# basic_salary, hra, da = 70000, 15000, 8000
# total_salary = basic_salary + hra + da
# print(f"Total salary: {total_salary}")


# basic_salary, hra, da = 90000, 15000, 8000
# bonus = 5000
# total_salary = calculate_salary(50000, 10000, 5000, 5000)  # arguments passed to the function
# print(f"Total salary: {total_salary}")



# basic_salary, hra, da = 80000, 15000, 8000
# total_salary = calculate_salary(basic_salary, hra, da, 0,2000)  # arguments passed to the function
# print(f"Total salary: {total_salary}")
