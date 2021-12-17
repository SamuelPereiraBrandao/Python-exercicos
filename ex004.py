algo = input("Digite Algo:")
print(type(algo))
print("so tem espaço em branco?", algo.isspace())
print("Eh um numero?", algo.isnumeric())
print("Eh alfabetico?", algo.isalpha())
print(("Eh alfanumerico?",algo.isalnum()))
print("Esta em maiuscula?", algo.isupper())
print("Esta em minuscula?", algo.islower())
print(("Esta capitalizada?", algo.istitle()))


