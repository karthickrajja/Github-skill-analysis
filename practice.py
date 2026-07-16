import pandas as pd 
print("Hello world\n\nKarthick here")

a = 10
b = 201

a+a\
+b

v = "karthick raja"

print(len(v))

print(v[::-1])

print(v.find("r",1,4))

print(v.startswith("ka"))
print(v.endswith("raja"))
print(v.count('r'))


if v.startswith("ka"):
    print("start with ka")
else:
    print("does not with ka")

value = 10
 
if value%2 == 0:
    print("even")
elif value%2 == 1:
    print("odd")


mark = 77

if mark >= 90:
    print("A")
elif mark >= 75:
    print("B")
elif mark >= 60:
    print("c")
elif mark >- 40:
    print("D")
else:
    print("fail")


age = 20
BMI = 15

if age < 18:
    print('Not eligible')
elif (age >= 18) and (age <= 40) and (BMI < 25):
    print("Weight Training + Cardio")    
elif (age >= 18) and (age <= 40) and (BMI >= 25):
    print("Weight Loss Program")   
elif (age > 40) and (BMI < 28):
    print("Low Impact Training")  
elif (age > 40) and (BMI > 28):
    print("Medical Checkup Required") 

if age < 18:
    print('Not eligible')
elif  18 <= age <= 40 and BMI < 25:
    print("Weight Training + Cardio")   