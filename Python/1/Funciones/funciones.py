def suma_naturales(n):
    #Regresa la suma de n números naturales: S = 1+2+3+...n
    s = 0
    for i in range(1, n + 1, 1):  # i no se está incrementando, está recorriendo el range
        s = s + i
    return s

def suma_naturales_to_string(n):
    #Regresa un string los números naturales: del 1 a n: 1, 2, 3, ...n
    msg = ""
    for i in range(1, n + 1, 1):  # i no se está incrementando, está recorriendo el range
        msg = msg + str(i)+", "
    return msg

def mcd(a, b):
    r = b%a   #calculo el residuo
    if(r == 0):
        return a
    else:
        return mcd(r, a)  #RECURSION

def suma_fracciones(a, b, c, d):
    '''a/b+c/d'''
    e = a*d + b*c
    f = b*d
    maxcd = mcd(e, f)
    e = e/maxcd
    f = f/maxcd
    return (e, f)

def fraccion_to_string(e, f):
    return (str(e)+"/"+str(f))

