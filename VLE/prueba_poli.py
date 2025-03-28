import Procedimientos as pr
C2=-4.3*0
C3=4.5
C4=-1.05
print(f'x^3 + {C2:2.2} * x^2 + {C3:2.2} * x + {C4:2.2}')
print('Interlos de raices',pr.evaluar_dominio(C2, C3, C4,(-5.0,5.0)))

raiz1, raiz2 = pr.max_min(C2,C3)
print('Raices de la derivada',raiz1,raiz2)
if (raiz1.imag==0 and raiz2.imag==0):
    if(raiz1.real==raiz2.real):
        # Esto creo que no es posible para un polinomio de grado 3
        print('La derivada tiene una única raiz real')
        print('El polinomio de grado 3 tiene un único óptimo')
        print('¿?')
    else:
        print('La derivada tiene dos raices reales')
        print('El polinomio de grado 3 tiene un máximo  y un mínimo')
else:
    print('La derivada no tiene raices reales')
    print('El polinomio de grado 3 no tiene óptimos')
