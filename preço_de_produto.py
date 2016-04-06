# Centro Universitário de João Pessoa - Unipê
# Redes de computadores P-2
# Algorítmos e Programação
# Professor: Jefferson Ferreira Barbosa
# Aluno: Marcos Alexandre Queiroz de Souza - Mat. 1520011782

# Programa preço de produtos

# preços = [float(input("Digite o preço do produto 1:")), float(input("Digite o preço do produto 2:")), float(input("Digite o preço do produto 3:")), float(input("Digite o preço do produto 4:")), float(input("Digite o preço do produto 5:"))]

precos = list()

for p in range (0, 5):
 precos.append(float(input("Digite o preço do Produto %d: " % (p + 1))))
 
inferior_50 = 0
entre_50_e_80 = 0
acima_de_80 = 0

media = ((preços [0]) + (preços [1]) + (preços [2]) + (preços[3]) + (preços[4])) / 5

for preco in precos:
	if preco < 50:
		inferior_50 = inferior_50 + 1
	if preco >= 50 and preco <= 80:
		entre_50_e_80 = entre_50_e_80 + 1
	if preco > 80:
		acima_de_80 = acima_de_80 + 1

print("Quantidade de produtos inferior a R$ 50,00 é: %d" % inferior_50)
print("Quantidade de produtos entre 50,00 e R$ 80,00 é: %d" % entre_50_e_80)
print("Quantidade de produtos acima de R$ 80,00 é: %d" % acima_de_80)
print("A média dos preços dos produtos é: R$ %.2f" %float(media))
