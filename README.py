v = float(input("digite o preço: "))

if v > 500:
    v = v * 0.98

else:
     v = v * 0.88


print(v)

while True:
     pergunta = str(input('Tem cupom Sim[s] ou Não [n]? ')).lower()
     if pergunta == ' ' or not pergunta in ['s','n']:
        v = v -50
     elif pergunta == 'n':
         print ("valor é", v)
