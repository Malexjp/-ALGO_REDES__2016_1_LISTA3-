# Centro Universitário de João Pessoa - Unipê
# Redes de computadores P-2
# Algorítmos e Programação
# Professor: Jefferson Ferreira Barbosa
# Aluno: Marcos Alexandre Queiroz de Souza - Mat. 1520011782

# Programa pesquisa de opinião

print("Qualifique o filme assistido seguindo os critérios: 1 - Regular; 2 - Bom; 3 - Ótimo")
opinioes = list()

for o in range (0, 3):
opinioes.append(int(input("Opinião do espectador %d: " % (o + 1))))

# opiniões = [int(input("Opinião do espectador 1:")), int(input("Opinião do espectador 2:")), int(input("Opinião do espectador 3:")), int(input("Opinião do espectador 4:")), int(input("Opinião do espectador 5:"))]

regular = 0
bom = 0
otimo = 0

for opinião in opiniões:
	if opinião == 1:
		regular = regular + 1
	if opinião == 2:
		bom = bom + 1
	if opinião == 3:
		otimo = otimo + 1

print("Quantidade de espectadores que opinaram regular: %d" % regular)
print("Quantidade de espectadores que opinaram bom: %d" % bom)
print("Quantidade de espectadores que opinaram ótimo: %d" % otimo)
