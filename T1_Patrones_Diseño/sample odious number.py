for n in range(0, 51): ## si Cantidad de unos es impar en binario es num odioso
    if bin(n).count('1') % 2 == 1:  #modulo <> 1 es impar
        print(n)