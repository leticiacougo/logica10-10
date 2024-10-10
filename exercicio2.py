def contar(string):
    string=string.replace(' ','')
    contador ={}
    for char in string:
        if char in contador:
            contador[char]+=1
        else:
            contador[char]=1
    return contador
palavra="ex de string com pontuação"
resultado=contar(palavra)
print(resultado)
