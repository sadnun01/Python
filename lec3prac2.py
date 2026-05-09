list1= input("Enter a list of numbers separated by commas: ").split(",")  
list2= input("Enter a list of numbers separated by commas: ").split(",")
copy_list1=list1.copy()
copy_list1.reverse()

if copy_list1==list2:
    print("Palindrome")
else:    print("Not Palindrome")    