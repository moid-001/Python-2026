#to check whether the given list is pallin`drome or not
list_1 = [1, 2, 3, 2, 1]
copy_list = list_1.copy()
copy_list.reverse()
if list_1 == copy_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")