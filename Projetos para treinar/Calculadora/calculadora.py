rodar = True


def separar_entrada(entrada):
    lista_entrada = []

    texto = ""
    for numero_caracter in range(0, len(entrada)):   
        
        if entrada[numero_caracter] == "+" or entrada[numero_caracter] == "-" or entrada[numero_caracter] == "*" or entrada[numero_caracter] == "/":
            lista_entrada.append(float(texto))
            lista_entrada.append(entrada[numero_caracter])
            texto = ""

        else:
            texto += entrada[numero_caracter]

    lista_entrada.append(float(texto))
    print(lista_entrada)
    return lista_entrada

def calcular(lista_entrada):
    lista_entrada
    for numero_posic in range(0, len(lista_entrada)):
        if "/" in lista_entrada or "*" in lista_entrada:
            # lista_entrada.find
            a = 0
        
while(rodar):
    entrada = input("Digite o calculo: ")
    
    if "e" in entrada:
        rodar = False
    
    lista_entrada = separar_entrada(entrada)
    calcular(lista_entrada)

    # entrada1 = float(input("Digite o primeiro valor: "))

    # print("+ -> Adição \n - -> Subtração \n * -> Multiplicação \n / -> Divisão")
    # calculo = input("Digite o calculo que deseja realizar: ")

    # entrada2 = float(input("Digite o segundo valor: "))

    # if "+" in calculo:
    #     resultado = entrada1 + entrada2

    # if "-" in calculo:
    #     resultado = entrada1 - entrada2

    # if "*" in calculo:
    #     resultado = entrada1 * entrada2

    # if "/" in calculo:
    #     resultado = entrada1 / entrada2

    # # entrada = input("Digite o calculo: ")

    # if entrada1 == "e" or entrada2 == "e":
    #     rodar = False

    # print(resultado)