def morning(name, ):
  print(f"Hallo, guys {name}")
  print("How are you today")
  print("im well this time")

morning("joe")



def sum(a,b):
  c = a + b
  d = a - b 
  e = a / b
  f = a % b
  return c , d , e, f

a = int(input("Enter value a = "))
b = int(input("Enter value b = "))

print("Your sum Value is ", sum(a, b)[0])
print("Your reduction Value is ", sum(a, b)[1])
print("Your multiplication Value is ", sum(a, b)[2])
print("Your division Value is ", sum(a, b)[3])
