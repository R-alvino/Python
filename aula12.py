nome = str(input('Qual é seu nome? '))
if nome ==  'Rafael':
    print("nome bonito!!! ")
elif nome == 'Pedro' or nome == 'Ana' :
    print('você tem um nome popular! ')   
else:
    print('Seu nome é bem normal. ')
print('Tenha um Bom Dia, {}'.format(nome))    