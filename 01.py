lista1 = []
lista2 = []
lista3 = []
lista4 = []

print('forneça um número. entre com um número negativo para finalizar o programa.')
n = int(input())


while n >= 0:
  if n < 26:
    lista1.append(n)
  elif n > 25 and n < 51:
    lista2.append(n)
  elif n > 50 and n < 76:
    lista3.append(n)
  elif n > 75 and n <= 100:
    lista4.append(n)
  else:
    print('Insira um número entre 0 e 100')  
  n = int(input('forneça um numero: '))

print("[0-25]: ", len(lista1))
print("[26-50]: ", len(lista2))
print("[51-75]: ", len(lista3))
print("[76-100]: ", len(lista4))
