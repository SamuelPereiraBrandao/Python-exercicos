nome = str(input("qual eh seu nome?"))
print("prazer em te conhecer {:=^20}".format(nome))
print("prazer em te conhecer {:>20}".format(nome))
print("prazer em te conhecer {:^20}".format(nome))
print("prazer em te conhecer {:<20}".format(nome))
# outra atividade
n1 = int(input("Um valor:"))
n2 = int(input("Outro valor:"))
print("O resultado da soma eh: {}".format(n1 + n2))

# outra atividade
n11 = int(input("primeiro numero:"))
n22 = int(input("segundo numero:"))
s = n11 + n22
m = n11 * n22
d = n11 // n22
di = n11 // n22
e = n11 ** n22
print("A soma eh {}, a multiplicacao eh: {} a divisao eh {:.3F}".format(s, m, d), end=" ")
print("a divisao inteiro eh: {} e a potencia eh: {}".format(di, e))
