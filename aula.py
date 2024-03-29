import matplotlib.pyplot as plt


x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="k", marker=".")
plt.plot(x, y, color="#000000", linestyle="--")
plt.legend()

plt.savefig("figura.png", dpi=1200)

#plt.show()