def ordenarBurbuja():
    valores = []
    i = 0
    ingreso = int(input("Cuantos elementos quiere ingresar a la lista? "))
    while i < ingreso:
        valor = int(input("Ingrese elementos a la lista!!"))
        valores.append(valor)
        i += 1
    print("La lista inicial era: " + str(valores))
    n = len(valores)
    for i in range(n-1):
        for j in range(n-1-i):
            if valores[j] > valores[j+1]:
                valores[j], valores[j+1] = valores[j+1], valores[j]
    print("La lista final es: " + str(valores))

ordenarBurbuja()