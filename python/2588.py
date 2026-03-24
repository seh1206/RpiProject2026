A = input()
B = input()

A= int(A)
B= int(B)

C = int(B//100)

D = int(B//10 - (C*10))

E = int(B-(C*100)-(D*10))

print(A*E)
print(A*D)
print(A*C)

print(A*B)
