def arif(num_1,num_2,num_3):
    print((num_1+num_2+num_3)/3)
arif(int(input()),int(input()),int(input()))
def NOD(num_1,num_2):
    while num_1 != 0 and num_2 !=0:
        if num_1>num_2:
            num_1 = num_1%num_2
        else:
            num_2 = num_2 % num_1
    print(num_1 + num_2)
NOD(int(input()),int(input()))
def triangle(a,A,B):
    C = 180 - A - B
    b = a*(A/(A + B))
    c = a *(B/(A+B))
    return b,c,C
b,c,C = triangle(a = float(input()),A = float(input()),B = float(input()))
print(f"b: {round(b,2)}, c: {round(c,2)},C: {round(C,2)}")
def comaretion(z,v):
    global n
    if z<v:
        n = v
    elif z>v:
        n = z
comaretion(int(input()),int(input()))
q = int(input())
w = int(input())
if q<w:
    if w>n:
        print(w)
    else:
        print(n)
else:
    if q>n:
        print(q)
    else:
        print(n)
