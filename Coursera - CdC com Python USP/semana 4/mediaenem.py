#MédiaEnem

print("==========================")
print("Simulação de média do ENEM")
print("==========================")

n = float(input("Natureza: "))
h = float(input("Humanas: "))
l = float(input("Linguagens: "))
m = float(input("Matemática: "))
Media1 = int((n + h + l + m) / 4)
r = int(input("Redação: "))
print("Sua média no ENEM é ", (Media1 + r)/2,".")