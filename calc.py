from calculadora import converterStringParaFloat, bitParaByte, byteParaBit,ByteParaKilobyte, KilobyteParaByte, kilobyteParaMegabyte, megabyteParaKilobyte, MegabyteParaGigabyte, gigabyteParaMegabyte, gigabyteParaTerabyte, terabyteParaGigabyte, terabyteParaPetabyte, petabyteParaTerabyte  

print(' Escreva 1 para bitParabyte \n Escreva 2 byteParaBit \n Escreva 3 byteParaKilobyte \n Escreva 4 kilobyteParaByte \n Escreva 5 kilobyteParaMegabyte \n Escreva 6 megabyteParaKilobyte \n Escreva 7 megabyteParaGigabyte \n Escreva 8 gigabyteParamegabyte \n Escreva 9 gigabyteParaTerabyte  \n Escreva 10 terabyteParaGigabyte \n Escreva 11 terabyteParaPetabyte \n Escreva 12 petabyteParaTerabyte')
funcEscolha = input()
if(funcEscolha == '1'):
    entradaDoTecladoValorAserConvertido  = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorAserConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    entradaDoTecladoValorAserConvertido = converterStringParaFloat (input())
    valorConvertido = byteParaBit(entradaDoTecladoValorAserConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    entradaDoTecladoValorAserConvertido = converterStringParaFloat (input())
    valorConvertido = ByteParaKilobyte(entradaDoTecladoValorAserConvertido)
    print(valorConvertido)

elif(funcEscolha) == '4':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat (input())
    valorConvertido = KilobyteParaByte(entradaDoTecladoValorAserConvertido)
    print(valorConvertido)

elif(funcEscolha) == '5':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat (input())
    valorConvertido = kilobyteParaMegabyte
    print(valorConvertido)

elif(funcEscolha) == '6':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat(input())
    valorConvertido = megabyteParaKilobyte
    print(valorConvertido)

elif(funcEscolha) == '7':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat(input())
    valorConvertido = MegabyteParaGigabyte
    print(valorConvertido)

elif(funcEscolha) == '8':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat(input())
    valorConvertido = gigabyteParaMegabyte
    print(valorConvertido)

elif(funcEscolha) == '9':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat(input())
    valorConvertido = gigabyteParaTerabyte
    print(valorConvertido)

elif(funcEscolha) == '10':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat(input())
    valorConvertido = terabyteParaGigabyte
    print(valorConvertido)

elif(funcEscolha) == '11':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat(input())
    valorConvertido = terabyteParaPetabyte
    print(valorConvertido)

elif(funcEscolha) == '12':
    entradaDoTecladoValorAserConvertido = converterStringParaFloat(input())
    valorConvertido = petabyteParaTerabyte
    print(valorConvertido)
