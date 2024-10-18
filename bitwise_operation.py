# user input 
a = int(input("Value a = "))
b = int(input("Value b = "))

# ALL OUTPUT WILL GENERATE TO BECAME BINER  

# AND Operation
and_result = a & b
print(f'Result for {a} & {b} is {bin(and_result)[2:].zfill(8)}')

# OR Operation
or_result = a | b 
print(f'Result for {a} | {b} is {bin(or_result)[2:].zfill(8)}')

# XOR Operation
xor_result = a ^ b
print(f'Result for {a} ^ {b} is {bin(xor_result)[2:].zfill(8)}')

#  NEGASI A Operation
neg_result_a= ~a
print(f'Result is ~{a} is {bin(neg_result_a)[2:].zfill(8)}')

#  NEGASI B Operation
neg_result_b = ~b
print(f'Result is ~{b} is {bin(neg_result_b)[2:].zfill(8)}')

# Left shift Operation
left = a << b
print(f'Result for {a} << {b} is {bin(left)[2:].zfill(8)}')

# Right shift Operation
right = a >> b
print(f'Result for {a} >> {b} is {bin(right)[2:].zfill(8)}')

