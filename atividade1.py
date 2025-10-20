#Desafio 1
#import calculadora

#print(calculadora())

#Desafio 2

def solicitar_numero():
    numero = int(input("Digite o numero: "))
    return numero

def gerar_tabuada (numero):
    tabuada = []
    for i in range(1,11):
        resultado = numero * i
        tabuada.append((numero, i, resultado))
    return tabuada

def exibir_tabuada(tabuada):
    print(f"\ntabuada do {tabuada[0][0]}")
    for numero, i, resultado in tabuada:
        print(f"{numero} x {i} = {resultado}")

def main():
    numero = solicitar_numero()
    tabuada = gerar_tabuada(numero)
    exibir_tabuada(tabuada)

if __name__ == "__main__":
    main()