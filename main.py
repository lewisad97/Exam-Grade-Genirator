import random

#Generates random marks between 0 and 100
marks = random.randint(0, 100)
print(marks)

if marks == 0 or marks < 35:
   print("Fail")
elif marks >= 35 and marks < 50:
   print("Grade C")
elif marks >= 50 and marks < 80:
   print("Grade B")
else:
   print("Grade A")
