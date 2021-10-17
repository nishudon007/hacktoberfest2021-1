A=float(input("enter the value of a: "))
B=float(input("enter the value of b: "))
C=float(input("enter the value of c: "))
D=(B**2)+(4*A*C)
if(D<0):
    print("no real roots exist")
if(D==0):
    R1=(-B)/(2*A)
    print("real and identical roots exists: ",R1)
if(D>0):
    R2=((-B)+(D**0.5))/(2*A)
    R3=((-B)+(D**0.5))/(2*A)
    print("real and distinct roots exists: ",R2,R3)
