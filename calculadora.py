def calculadora():

    valor_um = int(input("Informe o primeiro valor: "))
    operador = input("Informe a operação: (+,-<*,/)")
    valor_dois = int(input("Informe o segundo valor: "))

    if operador == "+":
        resultado = valor_um + valor_dois
        return resultado
    
    elif operador == "-":
        resultado = valor_um - valor_dois
        return resultado
    
    elif operador == "*":
        resultado = valor_um * valor_dois
        return resultado
    
    elif operador == "/":
        #Corrigindo o erro da divisão por zero
        if valor_dois == 0:
            print("Não é possivel a divisão por zero!")
        else:
            resultado = valor_um / valor_dois
            return resultado
    else:
        print("Operação não reconhecida")


print(calculadora())
    
