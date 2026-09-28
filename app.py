try:    
    # file = open("app.py")
    # age = int(input("Enter your age: ")) # system function to take input from user as int
    # if age <= 0:
    #     raise ValueError("Age cannot be zeror or less than zero")
    # elif age > 0:
    #     print("Test Message")

    # xfactor = 10 / age
    
    numbers = [10,20]
    print(numbers[1])
    
except (ValueError, ZeroDivisionError) as error:
    print("Please enter a valid integer for your age.")
    print(error) 
except IndexError as error:
    print("Please check your list donet have enough.")
    print(error) 
except Exception as error:
    print(type(error))   
else:
    print("Everuthing goes well") 
# finally:
#     # file.close()