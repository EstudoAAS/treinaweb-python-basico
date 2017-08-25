def somar(n1, n2):
    """Realiza a somatória de dois números"""
    print("{n1} + {n2} = {resultado}".format(n1 = n1,n2 = n2, resultado = n1 + n2))


def subtrair(n1, n2):
    """Realiza a subtração de dois números"""
    return n1 - n2


def multiplicar(n1, n2):
    """Realiza multiplicação de dois números"""
    return n1 * n2


def dividir(n1,n2):
    """Realiza a divisão de dois números, retornando o quociente e o resto"""
    return (n1//n2, n1%n2)


def media_aritmetica(*numeros):
    """Calcula a média aritmética dos números informados"""
    return sum(numeros) / len(numeros)