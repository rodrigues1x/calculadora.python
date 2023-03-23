def converterStringParaFloat(value):
    print('Valor convertido de str para float')
    return float(value)

def ByteParaKilobyte(valorASerConvertido):
    print('Valor convertido de byte para kilobyte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def KilobyteParaByte(valorASerConvertido):
    print('Valor convertido de Kilobyte para Byte')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = KilobyteParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)