#import funcoes_aritmeticas as arit
from matematica.funcoes_aritmeticas import somar,subtrair, multiplicar,dividir,media_aritmetica

numero1 = int(input("Digite o primeiro número: "))
operacao = input("Digite a operação: ")
numero2 = int(input("Digite o segundo número: "))
if operacao == "+":
    somar(numero1,numero2)
    print(somar.__doc__)
elif operacao == "-":
    resultado = subtrair(numero1, numero2)
    print("{n1} - {n2} = {resultado}".format(n1=numero1, n2=numero2, resultado=resultado))
elif operacao == "x":
    print("{n1} x {n2} = {resultado}".format(n1=numero1, n2=numero2, resultado=multiplicar(numero1,numero2)))
elif operacao == "/":
    quociente, resto = dividir(numero1,numero2)
    print("O quociente é: ", quociente, " e o resto é ", resto)

print("Média aritmética = {m}".format(m = media_aritmetica(3, 4, 5, 6)))
numeros = [10, 20, 30, 50, 60]
print("Outra média aritmética = {m}".format(m = media_aritmetica(*numeros)))