from math import sqrt, floor
import sys
import platform

def prob_1(n):
    return n%2 == 0

def prob_2(n):
    return (n-32)*(5/9)

def prob_3(n, b):
    if b == 0:
        return 1
    return n * prob_3(n, b-1)

def prob_4(c, l: int):
    size = len(c)
    final = ""

    if size == l:
        return c
    elif size > l:
        return "No puedes mandar un string mas grande que la longitud del parrafo"

    final = "*" * l
        
    if prob_1(l):
        half = int(l/2)
        if prob_1(size):
            half -= int(size/2)
            final = final[:half]
            print(final + c + final)
        else:
            half -= int((size+1)/2)
            final = final[:half]
            print(final + c + final + "*")
    else:
        half = int((l-1)/2)
        if prob_1(size):
            half -= int(size/2)
            final = final[:half]
            print(final + c + final + "*")
        else:
            half -= int(size/2)
            final = final[:half]
            print(final + c + final)
# PEP8
def prob_5(vect1, vect2):
    p1 = (vect1[1]*vect2[2]) - (vect1[2]*vect2[1])
    p2 = (vect1[0]*vect2[2]) - (vect1[2]*vect2[0])
    p3 = (vect1[0]*vect2[1]) - (vect1[1]*vect2[0])
    return [p1, -p2, p3]

def prob_6(lista):
    n = len(lista)
    for i in range(n):
        for x in range(0,n-i):
            if x+1 == n-i:
                break
            elif lista[x] < lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]
    return lista
    

def prob_7():
    lista = [x for x in range(1000) if x%4 == 0 or x%7 == 0]
    return lista

def prob_8(h):
    if h == 0:
        print("Altura no valida")
    elif h == 1:
        print("*")
    else:
        for i in range(h-1, 0, -1):
            space = " " * i
            ast = "* " * (h-i)
            print(space + ast)

def prob_9(num1, num2, num3):
    nums_sorted = [num1, num2, num3]
    nums_sorted.sort()
    return (nums_sorted[0]**2 + nums_sorted[1]**2) == nums_sorted[2]**2

# TODO Problema 10, triangulo, tuplas, tipo, coordenadas
def prob_10():
    pass

def prob_11(x):
    x = "".join(x.split())
    x = x.lower()
    n = len(x)
    for i in range(0,n-1):
        if x[i] != x[n-i-1]:
            return False
    
    return True

def prob_12(x):
    numbers = {1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",
               6:"seis",7:"siete",8:"ocho",9:"nueve",10:"diez",
               11:"once",12:"doce",13:"trece",14:"catorce",15:"quince",
               20:"veinte",30:"treinta",40:"cuarenta",50:"cincuenta",
               60:"sesenta",70:"setenta",80:"ochenda",90:"noventa",100:"ciento",
               200:"dos cientos",300:"tres cientos",400:"cuatro cientos",500:"quinientos",
               600:"seis cientos",700:"siete cientos",800:"ocho cientos",900:"novecientos",
               1000:"mil",0:"cero"}

    m = int(x/1000)
    n = x-m*1000
    c = int(n/100)
    n = n-c*100
    d = int(n/10)
    u = n-d*10

    if x == 100:
        return "cien"

    result = numbers.get(x, "Not Found")
    if result != "Not Found":
        return result
    
    result = ""
    if m != 0:
        result = numbers.get(m*1000)
        result += " "
    
    if c != 0:
        result += numbers.get(c*100) + " "
    
    if d != 0:
        result += numbers.get(d*10) + " "

    if u != 0:
        if c != 1:
            result += "y " + numbers.get(u)
        else:
            result += numbers.get(u)

    return result
    
def prob_13(x):
    total = 0
    for i in range(1, x):
        if x%i == 0:
            total += i

    return total

def prob_14(x):
    if x == 1:
        return False
    
    if x == 2 or x == 3:
        return True

    for i in range(2, x):
        if x%i == 0:
            return False

    return True

def prob_15(x):
    total = 0
    for i in range(1, x):
        if x%i == 0:
            total += i

    return x == total

def prob_16(x, r):
    totalX = 0
    totalR = 0
    for i in range(1, x):
        if x%i == 0:
            totalX += i
        if r%i == 0:
            totalR += i

    return totalX == r and totalR == x

def prob_17(a, b):
    divs_a = []
    for i in range(2, a):
        if a%i == 0:
            divs_a.append(i)

    for i in range(2, b):
        if b%i == 0 and i in divs_a:
            return False

    return True

def prob_18(n):
    x, y = 0, 1
    while x <= n:
        if x == n:
            return True
        x, y = y, x+y

    return False

def prob_19(n):
    x,y = 0,1
    while True:
        if len(str(x)) == n:
            return x
        x, y = y, x+y

def prob_20():
    lista = []
    for i in range(1, 1000):
        for j in range(i+1, 1000):
            a = j**2 - i**2
            b = 2*i*j
            c = i**2 + j**2
            if ((a**2 + b**2) == c**2) and (a + b + c) == 1000:
                lista.append([a,b,c])

    return lista

def prob_21(n):
    lista = []
    for i in range(2, n+1):
        if prob_14(i):
            lista.append(i)

    return lista

# TODO: Problema 22 cuadrado, tuplas, coordenadas
def prob_22():
    pass

def prob_23():
    path_delimiter = {"Windows":"\\", "Linux":"/", "Darwin":"/"}
    handle = open(sys.path[0] + path_delimiter.get(platform.system(), "/")  + "triangle.txt", "r")
    mapa =[]
    resultado = 0

    for line in handle:
        x = line.replace("\n", "")
        x = x.split(" ")
        mapa.append(x)
    
    pos = 0
    valores = []
    n = len(mapa)
    
    for i in range(n):
        if len(mapa[i]) == 1:
            valores.append(mapa[i][0])
            continue
        x = []
        if pos != 0:
            x.append(int(mapa[i][pos - 1]))
        if (pos + 1) != len(mapa[i]):
            x.append(int(mapa[i][pos + 1]))
        x.append(int(mapa[i][pos]))

        valores.append(max(x))

        if pos != 0:
            if x.index(max(x)) == 0:
                pos -= 1
            elif x.index(max(x)) == 1:
                pos += 1
        elif pos == 0 and len(mapa[i]) == 1:
            pos = 0
        else:
            if x.index(max(x)) == 0:
                pos += 1

    for i in valores:
        #print(i)
        resultado += int(i)

    return resultado


def prob_24(lista):
    v = lista
    lista_final = [v.copy()]
    ref = []
    n = len(v)

    for i in range(n):
        ref.append(0)

    p = 0

    while p < n:
        if ref[p] < p:
            if prob_1(p):
                v[0], v[p]= v[p], v[0]
            else:
                v[ref[p]], v[p] = v[p], v[ref[p]]
            lista_final.append(v.copy())
            ref[p] += 1

            p = 0
        else:
            ref[p] = 0
            p += 1

    return lista_final

if __name__ == '__main__':
    x = ""
    print(prob_1(100))
    print(prob_2(-12))
    print(prob_3(2,0))
    prob_4("holaa",11)
    print(prob_5([-3, -2, 5], [6, -10, -1]))
    print(prob_6([4,7,1,82,34,12,23,8,0]))
    print(prob_7())
    prob_8(5)
    print(prob_9(4, 5, 3))
    #print(prob_10())
    print(prob_11("Amad a la dama"))
    print(prob_12(101))
    print(prob_13(27))
    print(prob_14(19)) # 23452789
    print(prob_15(14))
    print(prob_16(220, 284))
    print(prob_17(9, 14))
    print(prob_18(6765))
    print(prob_19(3))
    print(prob_20())
    print(prob_21(109))
    #print(prob_22())
    print(prob_23())
    print(prob_24([1,2,3]))
