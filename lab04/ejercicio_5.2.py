#ejercicio 2

maximo = 0
minimo = 0
primer_numero = True
while True: 
    try: 
        input_str = input ("ingrese un numero:")
        if (input_str == "fin"):
            break
        else:
            if (primer_numero):
                maximo = int(input_str)
                minimo = int (input_str)
                primer_numero = False
            else:
                if(int(input_str)>maximo): maximo = int(input_str)
                if (int(input_str)< minimo): minimo = int (input_str)
    except:
        print("valor no es válido")
        continue
    print("maximo:", maximo)
    print("minimo:", minimo)
