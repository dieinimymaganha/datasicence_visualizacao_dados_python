# Crescimetno da População Brasileira 1980-2016
# DataSus
import matplotlib.pyplot as plt
dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

# Ignorando a primeira linha (range(len(dados)))
for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))


plt.bar(x, y, color="#E4E4E4")
plt.plot(x, y, color="k", linestyle="--")
plt.title("Crescimetno da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000")
# plt.show()
plt.savefig("Populacao_brasileira.png", dpi="300")
