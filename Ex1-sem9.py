import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    sab = abs(abs(as_a[0]-as_b[0])+abs(as_a[1]-as_b[1])+abs(as_a[2]-as_b[2])+abs(as_a[3]-as_b[3])+abs(as_a[4]-as_b[4])+abs(as_a[5]-as_b[5]))/6
    return sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    NTS = separa_sentencas(texto)
    NTF = []
    NTP = []
    SomTamPal = 0
    SomaPal = 0
    ListaPal = []
    NumPalDif = 0
    NumPalUni = 0
    somaFra = 0
    TamSent = 0
    TamFrase = 0
    
    for h in NTS:
        TamSent = TamSent + len(h)
    for z in NTS:
        NTF.append(separa_frases(z))
    for k in NTF:
        for i in k:
            NTP.append(separa_palavras(i))
    for i in NTP:
        for j in i:
            SomTamPal = SomTamPal + len(j)
    for a in NTP:
        SomaPal = SomaPal + len(a)
    for b in NTP:
        for c in b:
            ListaPal.append(c)
    for d in ListaPal:
        NumPalDif = n_palavras_diferentes(ListaPal)
    for e in ListaPal:
        NumPalUni = n_palavras_unicas(ListaPal)
    for f in NTF:
        for g in f:
            somaFra = somaFra + 1
    for l in NTF:
        for m in l:
            TamFrase = TamFrase + len(m)
    TamMedPal = (SomTamPal/SomaPal)
    TypeToken = (NumPalDif/SomaPal)
    HapaxLegomana = (NumPalUni/SomaPal)
    TamMedsen = (TamSent/len(NTS))
    ComplSen = somaFra/len(NTS)
    TamMedFra = (TamFrase/somaFra)
    assinatura = [TamMedPal, TypeToken, HapaxLegomana, TamMedsen, ComplSen, TamMedFra]
    print(assinatura)
    return assinatura
    

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assign = ass_cp
    txt = textos
    assinatura = []
    assimilaridade = []
    sab = 1000
    pos = 0
    for i in txt:
        assinatura.append(calcula_assinatura(i))
    for j in assinatura:
        assimilaridade.append(compara_assinatura(assign, j))
    for k in assimilaridade:
        if sab > k:
            sab = k
            pos = assimilaridade.index(sab) + 1
    return pos
    print("O autor do texto ",pos," está infectado com COH-PIAH")
avalia_textos(le_textos(), le_assinatura())
