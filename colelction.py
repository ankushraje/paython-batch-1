letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#letters.index(0,"_")
#finding the index of the letter "d" in the list
if "d" in letters:
    print("d is present in the list")
    print(letters.index("d"))
    
numbers = [3,51,2,8,6]
#numbers.sort() #sorting the list in ascending order
#numbers.sort(reverse=True) #sorting the list in descending order
sorted_numbers = sorted(numbers) #sorting the list in ascending order and returning a new list
print(numbers)
print(sorted_numbers)