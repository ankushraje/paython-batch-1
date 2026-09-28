num= 6
X="Weekend!" if num > 5 else "Weekday"
print(X)

x="Friday" if num == 5 else "Not Friday" if num==7 else "Not a special day"
print(x)

x=10+5 if num == 3 else 10-5
print(x)


#Ternanry Operators
#X="Block1" (condition) "Block2"
a=20
b=30
X="Sanika" if a>b else "Vishal"
print(X)

# == Equal
# != Not equal
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to


10==10 # output always true or false
print("10==10:", 10==10) # true
10!=11 # false
print(10!=10) # false
10>10 # false
print(10>10) # false
10>=10 # true
print(10>=10) # true
10<10 # false
print(10<10) # false
10<=10 # true
print(10<=10) # true


# Logical operator
# and &&
# or
# not

x = 5

# true and true = true
print(not(x>0 and x<10)) # false
print(x>10 or x<4) 
print(not(x>10 or x<4))

# Identity operator


# is 
# is not

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # true
print(x is y) # false
print (x == y) # false

# Membership operators
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # true
print("mango" not in fruits) # true 


#Bitwise operators
# &
# |
# <<
# >>>

# ()
# */
# +_

print((10+20)-5*(10+2))

# 30-60
# -30