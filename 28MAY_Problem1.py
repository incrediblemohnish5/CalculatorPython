print("CALCULATOR")

def add(a,b):
    return a+b

    
def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("NOT DEFINED")
    else:
        return a/b



while True:
    
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")

  if x==1:
        a=float(input("ENTER FIRST NUMBER"))
        b=float(input("ENTER SECOND NUMBER"))
        res=add(a,b)
        print(res)

    if x==2:
        a=float(input("ENTER FIRST NUMBER"))
        b=float(input("ENTER SECOND NUMBER"))
        res=sub(a,b)
        print(res)
        
    
    if x==3:
        a=float(input("ENTER FIRST NUMBER"))
        b=float(input("ENTER SECOND NUMBER"))
        res=mult(a,b)
        print(res)
        
    
    if x==4:
        a=float(input("ENTER FIRST NUMBER"))
        b=float(input("ENTER SECOND NUMBER"))
        res=divide(a,b)
        print(res)
