import math       
A = [[4,10],[5,6]]

a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]
trace = a + d
det = a * d - b * c

discriminant = trace ** 2 - 4 * det

if discriminant < 0:
    print("Complex eigenvalues are not handled.")
else:
    lambda1 = (trace + math.sqrt(discriminant)) / 2
    lambda2 = (trace - math.sqrt(discriminant)) / 2

    print("\nEigenvalues:")
    print("λ1 =", lambda1)
    print("λ2 =", lambda2)

    print("\nEigenvectors:")

    for lam in [lambda1, lambda2]:
 

        if abs(b) > 1e-10:
            x = 1
            y = -(a - lam) / b

        elif abs(c) > 1e-10:
            y = 1
            x = -(d - lam) / c

        else:
            x = 1
            y = 0

        print("For λ =", lam)
        print("[", x, ",", y, "]")
        
        
        
        
        
        
        
        
        
        
