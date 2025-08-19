#Read three angles of triangles and determine their types(Right, Obtuse , Acute triangle)

A = int(input("Enter angle A: "))
B = int(input("Enter angle B: "))
C = int(input("Enter angle C: "))

if( A + B + C == 180 and A > 0 and B > 0 and C > 0 ):
    if A == 90 or B == 90 or C == 90:
        print("It is a Right-angled triangle.")
    elif A > 90 or B > 90 or C > 90:
        print("It is an Obtuse triangle.")
    else:
        print("It is an Acute triangle.")
else:
    print("Not a valid triangle.")