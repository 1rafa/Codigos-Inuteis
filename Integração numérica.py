"""
Não use nada disso. Use numpy.integ() no lugar.

"""

def f(x):
    return x**2-3


def Simpson(função, n, a, b):
    '''
    Calcula a integral da função pelo método numérico 1/3 de simpson
    função: uma função que retorna os valores da função que queremos integrar
    n: o número de divisões que faremos na função
    a: o limite inferior do intervalo de integração
    b: o limite superior do intervalo de integração
    Is: a integral aproximada da função
    retorna um número (float)
    '''
    f = função
    h = (b-a)/n
    Is = (h/3)*(f(a)+f(b))

    for i in range(n):
        c = a+(i*h)
        if i % 2 == 0 :		# “i % 2 == 0” testa se i é par ou ímpar
            Is = Is + (h/3)*2*f(c)
        else:
            Is = Is + (h/3)*4*f(c)
    return Is

def métodoDoTrapézio(função, n, a, b):
    '''
    Calcula a integral da função pelo método numérico do trapézio
    função: uma função que retorna os valores da função que queremos integrar
    n: o número de divisões que faremos na função
    a: o limite inferior do intervalo de integração
    b: o limite superior do intervalo de integração
    Is: a integral aproximada da função
    retorna um número (float)
    '''
    f = função
    h = (b-a)/n			# “h” guarda a distância entre xi e x(i+1)
    It = h*(f(a)+f(b))/2 	#“It” é a integral aproximada (numericamente) da função

    for i in range(n):
        c = a+(i*h)
        It = It + f(c)*h
    return It