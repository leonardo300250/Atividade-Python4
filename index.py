import meu_modulo
import cabecalho

#cabeçalho da página
cabecalho.header()

resultado = meu_modulo.multiplicacao(4,2)
saudacao = meu_modulo.saudacao("Leonardo")
print(resultado)
print(saudacao)

cabecalho.footer()