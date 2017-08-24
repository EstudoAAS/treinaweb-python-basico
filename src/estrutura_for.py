numero = int(input("Digite um número: "))
#print(range(11))
for i in range(11):
    print("{n} x {i} = {resultado}".format(n = numero, i = i, resultado = numero * i))
else:
    print(" ** Processo concluído **")

linguagens = ["Python", "C#", "PHP", "Java"]
print("Algumas linguagens de programação são: ")
for linguagem in linguagens:
    print(" - " + linguagem)

capitais = {"SP":"São Paulo", "RJ":"Rio de Janeiro", "MG":"Belo Horizonte", "TO":"Palmas", "AM":"Manaus"}
print("Algumas capitais do Brasil são: ")
for sigla,capital in capitais.items():
    print(" - {sigla}: {capital}".format(sigla = sigla, capital = capital))