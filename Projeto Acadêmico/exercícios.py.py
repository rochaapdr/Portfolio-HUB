#1.	Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário. Onde: volume = 4/3*pi*r3
raio = float(input(f'Digite (em centímetros) o raio de uma esfera para descobrir seu volume: '))
pi = 3.14
volume = 4/3 * pi * raio**3  

print(f'O volume da esfera de raio {raio:.0f}, é {volume:.2f}cm^3')

#2. - A água é um nutriente essencial. Sem ela, o corpo não pode funcionar com perfeição. Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo.
#A dose ideal, ou seja, a necessidade diária em litros é calculada através da fórmula: massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo.

massa = float(input("Para saber a quantidade de água ideal, digite seu peso (em kg): "))
litros = float(massa * 0.03)

print(f"A quantidade de água ideal para seu corpo é {litros} litros")

#3. Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles. Use a seguinte fórmula:
#distância =  √((x_2-〖x_1)〗^2+〖(y_2-〖y_1〗_ )〗^2 ) 

print('No Plano cartesiano, descubra a distancia entre os pontos P e Q.')

x1 = int(input('Digite o X1 de P: '))
y1 = int(input('Digite o Y1 de P: '))
x2 = int(input('Digite o X2 de Q: '))
y2 = int(input('Digite o Y2 de Q: '))
distancia = (((x2 - x1)*2 + (y2 - y1)*2))

print(f'A distancia entre os pontos P e Q é de: {distancia:.0f}')

#4. Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os valores serão fornecidos pelo usuário. 
print("Para descobrir a ordem crescente entre dois números, digite abaixo:\n")
n1 = int(input("Digite o valor do primeiro número: "))
n2 = int(input("Digite o valor do segundo número: "))

if n1 > n2:
    print(f"A ordem crescente desses valores é {n2},{n1}.")

elif n1 < n2:
    print(f"A ordem crescente desses valores é {n1},{n2}.")

else:
    print("Os valores são iguais.")

#5. Construa o programa que calcule o peso ideal de uma pessoa.
# Utilize as seguintes fórmulas:
#- Se homem, o peso ideal é calculado assim: (72,7 x altura) - 58;
#- Se mulher, o peso ideal é calculado assim: (62,1 x altura) - 44,7.
#Analise o problema e verifique quais são os dados que o usuário precisa fornecer (digitar).

altura = float(input('Para descobrir seu peso ideal, digite sua altura em metros (exemplo: 1.80): '))
         
print(f'Qual seu gênero?','\n( 1 ) Masculino \n( 2 ) Feminino')
genero = int(input('Digite: '))

if genero == 2:
    print(f'O peso ideal para você é {(62.1 * altura) - 44.7:.2f}kg')
else:
    print(f'O peso ideal para você é {(72.7 * altura) - 58:.2f}kg')
