#Program for Reading the Values from KeyBoard by using Comprehension Concept
#ListCompEx2.py
print("Enter List of Values Separated by Space:")
lst=[  float(val)       for val in input().split()     ]  # List Comprehension
print("List of Values")
print(lst)