nome = str(input('Digite seu nome completo: ')).strip()
print(nome)
print("Seu nome em Maiusculo é ", nome.upper())
print("Seu nome emminusculo é ", nome.lower())
print("Seu nome tem ao todo em letras", len(nome) - nome.count(' '))
#print("Seu primeiro nome tem tantas letras", nome.find(' ') )
separa = nome.split()
print('Seu primeiro nome é {}, e ele tem {} letras'.format(separa[0], len(separa[0])))