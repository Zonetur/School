import math
PI = math.pi

print('a - Pp Kola | b - Obw kola w cm')

inp = input()
if 'a' == inp:
    r = float(input())
    print("pole powierzchni kola wynosi " + str(PI*r**2) + "cm")
elif 'b' == inp:
    r = float(input())
    print("obwód kola wynosi " + str(2*PI*r) + "cm²")
else:
    print('Nie ma takiej operacji')
