import time

print("Informe os valores de a, b e c na equação de segundo grau")
while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    print(f'Equação: {a}x^2 + {b}x + {c} = 0')
    time.sleep(2)

    # DELTA
    D = b**2 - 4*a*c
    print(f'Delta: {D:.2f}')
    time.sleep(2)

    # Verificação se Delta é negativo
    if D < 0:
        print("Delta negativo, a equação não possui raízes reais.")
    else:
        # X1 e X2
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)
        print(f'X1 = {x1:.2f}')
        print(f'X2 = {x2:.2f}')
        
    time.sleep(2)

    final = input('Digite: \n(1) para continuar \n(2) para finalizar \n:')
    if final == '2':
        break
