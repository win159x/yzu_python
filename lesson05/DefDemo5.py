x = 0 #global var
y = 0 #global var
z=[0]
def changeX(n):
    x = n #local var

def changeY(n):
    global y
    y = n #local var

def changeZ(m, n):
    m[0] = n

print("x=", x)
changeX(100)
print("x=", x)

print("y=", y)
changeY(100)
print("y=", y)

print("z=", z)
changeZ(z, 100)
print("z=", z)