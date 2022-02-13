import matplotlib.pyplot as plt

def f1(x):
    return 2*(x**2) + 5*x - 2
# Función lineal.
def f2(x):
    return 4*x + 1
# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
plt.plot(x, [f1(i) for i in x])
plt.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")
# Limitar los valores de los ejes.
plt.xlim(-10, 10)
plt.ylim(-10, 10)
#plt.autoscale() Autoscale
#Labels
plt.xlabel('some numbers')
plt.ylabel('some numbers')
# Guardar gráfico como imágen PNG.
plt.savefig("output.png")
# Mostrarlo.
plt.show()