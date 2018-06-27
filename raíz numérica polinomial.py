"""
Não use nada disso. Use numpy.roots() no lugar.
"""


import numpy as np

def bisseção(fPoli,limInf, limSup, precisão = 0.01):
    """
    Método para ser usado na função raizNuméricaPolinomial().
    Encontra uma raíz de fPoli, entre limInf e limSup, com dada precisão.
    fpoli: uma função polinomial do tipo np.poly1d()
    limInf, limSup: números inteiros
    return: uma única raíz da função
    """
    a1 = limInf
    a2 = limSup
    while True:
        m = (a1+a2)/2
        K1 = fPoli(a1)
        K2 = fPoli(a2)
        K3 = fPoli(m)
        if K1 == 0:
            return a1
        if K2 == 0:
            return a2
        if K3 == 0:
            return m
        if (K1>0 and K3<0) or (K1<0 and K3>0):
            a2 = m
        elif (K2>0 and K3<0) or (K2<0 and K3>0):
            a1 = m
        if (abs(K1-K2)) < precisão:
            return a1, a2

def falsaPosição(fPoli,limInf, limSup, precisão = 0.01):
    """
    Método para ser usado na função raizNuméricaPolinomial().
    Encontra uma raíz de fPoli, entre limInf e limSup, com dada precisão.
    fpoli: uma função polinomial do tipo np.poly1d()
    limInf, limSup: números inteiros
    return: uma única raíz da função
    """
    a1 = limInf
    a2 = limSup
    while True:
        K1 = fPoli(a1)
        K2 = fPoli(a2)
        m = (a1*K2-a2*K1)/(K2-K1)
        K3 = fPoli(m)
        if K1 == 0:
            return a1
        if K2 == 0:
            return a2
        if K3 == 0:
            return m
        if (K1>0 and K3<0) or (K1<0 and K3>0):
            a2 = m
        elif (K2>0 and K3<0) or (K2<0 and K3>0):
            a1 = m
        if (abs(K1-K2)) < precisão:
            return a1, a2
            
def newtonRalphson(fPoli,limInf, limSup, precisão = 0.01):
    """
    Método para ser usado na função raizNuméricaPolinomial().
    Encontra uma raíz de fPoli, entre limInf e limSup, com dada precisão.
    fpoli: uma função polinomial do tipo np.poly1d()
    limInf, limSup: números inteiros
    return: uma única raíz da função
    """
    a1 = limInf
    dPoli = fPoli.deriv()
    while True:
        K1 = fPoli(a1)
        dK1 = dPoli(a1)
        m = a1-(K1/dK1)
        if (abs(a1-m))<0.01:
            return a1
        a1 = m

def raizNuméricaPolinomial(lista, método, chute = 0, inter = 1, soma = 10):
    """
    Acha somente uma raíz de uma função polinomial qualquer
    Para o código funcionar, só pode haver uma raíz entre limSup e limInf
    lista: lista com os parâmetros da função
    método: função que representa o método a ser usado para encontrar a raiz
    return: limites inferior e superior que contém uma única raíz da função
    """
    fPoli = np.poly1d(lista)
    while True:
        limSup = chute + inter
        limInf = chute - inter
        if (fPoli(limInf)>=0 and fPoli(limSup)<=0) or (fPoli(limInf)<=0 and fPoli(limSup)>=0):
            return método(fPoli,limInf, limSup)
        else:
            inter += soma


lista = [-2,1,6]
print( raizNuméricaPolinomial(lista, falsaPosição, 2.1, 0.5, 0.1) )