import random

# variabel
welcome_message = "Welcome To Mouse Game"
mouse_position = random.randint(1, 4)

print("===========================")
print(f'== {welcome_message} ==')
print("===========================")

# input condition
user_name = input("What's Your Name: ")
print(f'''Hallooo, {user_name}!! Choose a hole where the rat is likely to be inside
      (_) (_) (_) (_) 
       1   2   3   4
      ''')
result_user = input("Where do rats hide [1 or 2 or 3 or 4]: ")

# if else condition
if int(result_user) == mouse_position: 
  print(f'Your Choose is {result_user}, Congratulations on your choice, the rat is in {mouse_position} position')
else:
  print(f'Your answer is wrong, the rat is in {mouse_position} position')
