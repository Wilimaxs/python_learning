# samplel 1
sum = 0
for i in range(1,11):
  sum = sum + i
print(sum)

print("==========================================================")

# sampel 2
fruit_list = ["grape", "watermelon", "strowberry"]
for i in fruit_list:
  print(i, end= ", ")
print("")
print("==========================================================")

# sampel 3
for i in range(1, 10, 2):
  print("Range number with 2 step: ", i)

print("==========================================================")

# sampel 4
value = int(input("Enter your value: "))
custom_range = int(input("Enter your custom range: "))
for i in range(1, custom_range + 1):
  mul = value * i
  print(f'{value} * {i} = {mul}')
  
# sampel 5
list = ["C++", "JS", "python", "GO"]
for i in range(len(list)):
  print("Hello " + list[i])
  
# sample 6 (NASTED LOOPING))
companies = ["GOOGLE", "APPLE", "AMAZON", "TIKTOK"]
for i in companies:
  print("the compony name is "+i)
  for letter in i:
    print(letter)
    
# sample 7
for i in range(1, 11, 3):
  print(i)
else:
  print("Looping has completed")
  
# sample 8
for i in range(1, 11):
  if (i == 6):
    break
  print(i)

# sample 9 
player_name = "wawan"
list_goals = {"xiangling": 8, "wawan" : 9, "sarimin": 23}
for i in list_goals:
  if i == player_name:
    print(list_goals[i])
    break
else:
  print("player not found")
  
# sample 10
num = [2,5,7,4,8,6]
cube = []
for i in num:
  cube.append(i**3)
  print(cube)
print(cube)

# sample 11
value = int(input("Enter for custom length: "))
for i in range(0, value):
  for j in range(0, i+1):
    print("*", end="")
  print("")

# sample 12 
count = 0
while count <= 10:
  print("belom")
  count+=1

# sample 13
num = 0
count = 0
sum = 0
while num >= 0:
  num = int(input("input your positive number: "))
  if (num >= 0):
    count = count + 1
    sum = sum + num 
avg = sum / count
print("Total Sum Of Number is ", sum, "Average ", avg, "count", count )

# sample 14
import random
n = random.randint(1,100)
print(n)
guess = int(input("Guees the number between 1 to 100: "))
while n != guess:
  if (guess < n):
    print("Your guess number is too low")
    guess = int(input("Guess the number between 1 to 100: "))
  elif (guess > n):
    print("Your guess number is too high")
    guess = int(input("Guess Ther number between 1 to 100: "))
else:
  print("thats correct numeber")

# sample 15
list_fruit = ["manggo", "grape", "watermalon", "orange"]
for fruit in list_fruit:
  for i in fruit:
    print(i,end=",")
  print()

# sample 16
list_fruit = ["manggo", "grape", "watermelon", "orange"]
list_color = ["red", "blue", "green"]
for i in list_color:
  for j in list_fruit:
    print(i,j, end="#")
    print()
  print()

# sample 17
for i in range(1,11):
  for j in range(i):
    print("*", end= " ")
  print()

# sample 18
i = 11
while (i > 0):
  j = 11
  while(j >= i):
    print("*", end=" ")
    j -= 1
  i -= 1
  print()

# sample 19
i = 11
while (i > 0):
  j = 1
  while(j <= i):
    print("*", end=" ")
    j += 1
  i -= 1
  print()

# sample 20
list1 = [10,20,30]
list2 = [50,60,70]
result = []
for i in list1:
  for j in list2:
    result = i + j
    print(result, end=", ")

# sample 21
list1 = [10,20,30]
list2 = [50,60,70]
result = []
for i in list1:
  for j in list2:
    result.append(i+j)
print(result)

# sample 22
list1 = [2, 3, 4]
list2 = [2, 3, 4]
for i in list1:
  for j in list2:
    if i == j :
      continue
    print(i, " * ", j, "= ", i*j)