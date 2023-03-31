altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg:'))
imc = peso /(altura/100)**2
 

if imc <= 18.5:
    print(f'O valor do seu IMC é: {imc:.2f} e é classificado como: Baixo peso.\n Procure auxilio de uma nutricionista: Amanda Alves')
elif imc >= 18.5 and imc <= 24.99: 
    print (f'O valor do seu IMC é:{imc:.2f} e é classificado como: Normal.\n Procure auxilio de uma nutricionista: Amanda Alves') 
elif imc >=24.99 and imc <=29.99: 
    print (f'O valor do seu IMC é: {imc:.2f} e é classificado como: Sobrepeso.\n Procure auxilio de uma nutricionista: Amanda Alves') 
elif imc >=30 and imc <= 39.99: 
    print (f'O valor do seu IMC é: {imc:.2f} e é classificado como: Obesidade\n Procure auxilio de uma nutricionista: Amanda Alves')
else: 
    print('Procure ajuda de uma nutricionista: Amanda Alves')


