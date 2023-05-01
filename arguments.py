# Write a Python function that takes two arguments (a and b) and returns their sum.
def add(a,b):
    answer = a+b
    return answer

# Write a Python function that takes a string as input and returns the string reversed.
# def reverse_slicing(s):
#     return s[::-1]
def reverse_string(word):
    list_string=list(word)
    list_string.reverse()
    return ''.join(list_string)

# Write a Python function that takes a list of integers as
#  input and returns the sum of all the integers in the list.
def list_integers(nums):
    total=0
    for x in nums:
        total+= x
    return total
    
# Write a Python function that takes a list of integers as 
# input and returns a new list with all the even numbers removed.
# list = [2, 4, 6, 8, 10]
def integers_list(list):
  empty_arr=[]
  for x in list:
      if x %2 !=0:
          empty_arr.append(x)
  return empty_arr

# Write a Python function that takes a list of integers as input 
# and returns the highest value in the list.
def list_integers(numbers):
    max=numbers[0]
    for num in numbers:
        if num>max:
            max=num
    return max
num=[3,4,5,6,7,8]
print(list_integers(numbers))

# Write a Python function that takes a list of strings as input and
#  returns a new list with all the strings capitalized.
def list_string(strings):
    return [s.capitalize()for s in names]

strings=["faith","glenah","feli"]
print(list_string(strings))

  