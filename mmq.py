"""
Não use nada disso. Use numpy.polyfit no lugar.
"""

def getG(string, x):
    """
    calcula o valor de Y, para função de X, dado uma String que representa a função
    """
    y = string
    z = eval(y)
    return z

def MMQ(m, y, g1, g2):
    '''
    calcula a curva de regressão de uma certa função pelo método dos mínimos
    quadrados.
    m: lista dos valores observados de x
    y: lista dos valores observados de f(x)
    g1: uma função
    g2: uma função
    G(x) é a função aproximada de f(x), onde: f(x)≈ G(x)= c1*g1(x)+ c2*g2(x)
    '''
    def p1(u,v):
        """
        retorna o produto interno entre as funções u e v.
        """
        z = 0
        for i in range(len(m)):
            z += u(m[i])*v(m[i])
        return z
    
    def p2(u):
        """
        retorna o produto interno entre uma função u e os valores observados.
        """
        z = 0
        for i in range(len(m)):
            z = z + u(m[i])*(y[i])
        return z

    c2 = (p2(g1)*p1(g1,g2)-p1(g1,g1)*p2(g2))/(p1(g1,g2)**2-p1(g1,g1)*p1(g2,g2))
    c1 = ((p2(g1))-(p1(g1,g2)*c2))/(p1(g1,g1))
    return c1, c2