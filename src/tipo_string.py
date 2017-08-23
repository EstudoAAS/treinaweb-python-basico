string_1 = 'Isso é uma string'
print("String 1: ")
print(string_1)
string_2 = "Isso é outra string"
print("String 2: ")
print(string_2)

string_1 = 'Redefini a \' minha string_1'
string_2 = "Redefini a ' outra string"
print("Primeira string modificada:")
print(string_1)
print("Segunda string modificada:")
print(string_2)

string_3 = '''Isso é mais uma string " '
Outro texto
Mais uma linha denovo
    Teste teste'''
print("String 3: ")
print(string_3)

print(" *** Operações com strings ***")
string_a = "Hello "
string_b = "World"
print(string_a + string_b)
print((string_a + string_b) * 3)
print(string_a[0])
print(string_b[len(string_b) - 1])
print(string_b[-2])
print(string_b[1:4])
print(string_b[1:])
print(string_b[:3])