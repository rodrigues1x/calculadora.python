from calc import converterStringparaFloat,megabyteParaGigabyte, gigabyteParaMegabyte

print(' Escreva 1 para megabyteParaGigabyte \n Escreva 2 gigabyteParaMegabyte')
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorAserConvertido  = converterStringparaFloat(input())
    valorConvertido = megabyteParaGigabyte(entradaDoTecladoValorAserConvertido)
    print(valorConvertido)


