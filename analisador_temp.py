# Monitoramento de temperatura para laboratórios
# Desenvolvido por: Everton M. (Engenharia de Computação - IFRJ)

tempalta = []
tempbaixa = []
tempnorma = []

def analise_temperatura():
    while True:
        temp = float(input("Digite as temperaturas atuais do lab ou digite 999 para sair: "))
        if temp == 999:
            break
        elif temp >= 50:
            print("Alta temperatura registrada")
            tempalta.append(temp)
        elif temp <= 0:
            print("temperatura baixa")
            tempbaixa.append(temp)
        else: 
            print("temperatura padrão")
            tempnorma.append(temp)

analise_temperatura()

def media_temp():
    mediaalta = sum(tempalta) / len(tempalta) if len(tempalta) > 0 else 0
    mediabaixa = sum(tempbaixa) / len(tempbaixa) if len(tempbaixa) > 0 else 0
    medianorm = sum(tempnorma) / len(tempnorma) if len(tempnorma) > 0 else 0
    return mediaalta , mediabaixa , medianorm

if len(tempalta) == 0 and len(tempbaixa) == 0 and len(tempnorma) == 0:
    print("nenhuma temperatura foi registrada")
else:    
    mediaalt , mediabx , medianor = media_temp()

    def resultados():
        print(f"a temperaturas altas foram {len(tempalta)} é sua media foi {mediaalt:.2f}")
        print(f"a temperaturas baixas foram {len(tempbaixa)} é sua media foi {mediabx:.2f}")
        print(f"a temperaturas normais foram {len(tempnorma)} é sua media foi {medianor:.2f}")

    def quantidadelist():
        print(f"temperaturas altas registradas foram: {tempalta}") 
        print(f"temperatuas baixas registradas foram: {tempbaixa}")
        print(f"temperaturas normais registradas foram: {tempnorma}")

    resultados()
    quantidadelist()
