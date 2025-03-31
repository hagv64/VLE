import Procedimientos as pr
C2=-4.3*0
C3=4.5
C4=-1.05
intervalos=[]
print()
print(f'x^3 + {C2:2.2} * x^2 + {C3:2.2} * x + {C4:2.2}')
intervalos = pr.evaluar_dominio(C2, C3, C4,(-5.0,5.0))
print('Interlos de raices de polinomio de tercer grado', intervalos)
maxmin1, maxmin2 = pr.max_min(C2,C3)
print()
print('Raices de la derivada',maxmin1,maxmin2)
if (maxmin1.imag==0 and maxmin2.imag==0):
    if(maxmin1.real==maxmin2.real):
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
print()
print("Raices del polinomio de tercer grado")
raiz=[]
for i in range(3):
    if intervalos[i]!=tuple():
        raiz.insert(i,pr.Newton_Raphson(intervalos[i],C2,C3,C4))
        print(f"Raiz[{i}] =", raiz[i])

