#Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C. 

A = float(input("Enter number A: "))
B = float(input("Enter number B: "))
C = float(input("Enter number C: "))

if A <= B and A <= C:
    minimum = A
elif B <= A and B <= C:
    minimum = B
else:
    minimum = C

print("The minimum number is:", minimum)

