# Procedimientos para resolver los ceros un polinomio cúbico y = X ** 3 + C2 * X ** 2 + C3 * X + C4
# Usando Newton-Raphson
# Derivada de un polinomio cúbico
from cmath import sqrt


def derivada(x, C2, C3):
    return 3 * x ** 2 + 2 * C2 + C3


# Polinomio cúbico con el término
def polinomio(x, C2, C3, C4):
    return x ** 3 + C2 * x ** 2 + C3 * x + C4


def Newton_Raphson(rango_x, C2, C3, C4, epsilon=0.00001, max_iter=100):
    n = 1
    x0 = rango_x[0]
    while n < max_iter:
        x1 = x0 - polinomio(x0, C2, C3, C4) / derivada(x0, C2, C3)
        if abs(x1 - x0) <= epsilon:
            return x1
        x0 = x1
    n = 1
    x0 = rango_x[1]
    while n < max_iter:
        x
        x1 = x0 - polinomio(x0, C2, C3, C4) / derivada(x0, C2, C3)
        if abs(x1 - x0) <= epsilon:
            return x1
        x0 = x1
    return None


# Máximo y mínimo de la ecuación cúbica
def max_min(C2, C3):
# La derivada es y'= 3 * x ** 2 + 2 * C2 * x + C3
    discriminante_cuarto = C2 ** 2 - 3 * C3
    if discriminante_cuarto < 0:
        return complex(-C2 / 3, sqrt(-discriminante_cuarto) / 3), complex(-C2 / 3, -sqrt(-discriminante_cuarto) / 3)
    elif discriminante_cuarto == 0:
        return complex(-C2 / 3, 0), complex(-C2 / 3, 0)
    elif discriminante_cuarto > 0:
        return complex(-C2 / 3 + sqrt(discriminante_cuarto) / 3), complex(-C2 / 3 - sqrt(discriminante_cuarto) / 3)

# Evaluación del polinomio en un sub-dominio
def evaluar_dominio(C2, C3, C4, dominio_acotado=(0.0, 6.0), paso=0.001):
    x0 = dominio_acotado[0]
    intervalos = [(), (), ()]
    n_intervalos = 0
    while(x0 <= dominio_acotado[1]):
        y0 = polinomio(x0,C2,C3,C4)
        x1 = x0 + paso
        y1 = polinomio(x1,C2,C3,C4)
        if (y0 * y1 < 0):
            intervalos[n_intervalos] = (x0, x1)
            n_intervalos += 1
        x0 += paso
    return intervalos

# Debe devolver tres intervalos, un intervalos de cambio de signo (los otros dos nulos)
# o tres cambios de signo
# Si devuelve solo un intervalos válido se debe revisar si uno de los valores
# óptimos es un cero del polinomio
