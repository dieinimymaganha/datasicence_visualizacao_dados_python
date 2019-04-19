import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

# Titulo
plt.title("Meu primeiro gráfico com Python")

# Eixos

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()