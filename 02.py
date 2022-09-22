preco_100 = 1.2
preco_101 = 1.3
preco_102 = 1.5
preco_103 = 1.2
preco_104 = 1.3
preco_105 = 1

quant_100 = 0
quant_101 = 0
quant_102 = 0
quant_103 = 0
quant_104 = 0
quant_105 = 0

total = 0

print(
    "Produto         Codigo  Preço"
    "\n-------------------------------"
    "\nCachorro Quente 100     R$ 1.20"
    "\nBauru Simples   101     R$ 1.30"
    "\nBauru com ovo   102     R$ 1.50"
    "\nHamburguer      103     R$ 1.20"
    "\nCheeseburguer   104     R$ 1.30"
    "\nRefrigerante    105     R$ 1.00\n"
)

codigo = 1
while codigo != 0:
  codigo = int(input('Entre com o código do produto (ou com 0 para encerrar o pedido).'))
  if codigo < 100 or codigo > 105:
    if codigo != 0:
      print('Código inválido.')
    continue
  quantidade = int(input('Entre com a quantidade desse produto.'))
  if codigo == 100:
    quant_100 += quantidade
  elif codigo == 101:
    quant_101 += quantidade
  elif codigo == 102:
    quant_102 += quantidade
  elif codigo == 103:
    quant_103 += quantidade
  elif codigo == 104:
    quant_104 += quantidade
  elif codigo == 105:
    quant_105 += quantidade


print('Fechamento do pedido')

if quant_100 > 0:
  print('Cachorro Quente: ', quant_100, 'unidades. R$ %.2f' %(quant_100 * preco_100))
  total += quant_100 * preco_100
if quant_101 > 0:
  print('Bauru Simples: ', quant_101, 'unidades. R$ %.2f' %(quant_101 * preco_101))
  total += quant_101 * preco_101
if quant_102 > 0:
  print('Bauru com ovo: ', quant_102, 'unidades. R$ %.2f' %(quant_102 * preco_102))
  total += quant_102 * preco_102
if quant_103 > 0:
  print('Hamburguer: ', quant_103, 'unidades. R$ %.2f' %(quant_103 * preco_103))
  total += quant_103 * preco_103
if quant_104 > 0:
  print('Cheeseburguer: ', quant_104, 'unidades. R$ %.2f' %(quant_104 * preco_104))
  total += quant_104 * preco_104
if quant_105 > 0:
  print('Refrigerante: ', quant_105, 'unidades. R$ %.2f' %(quant_105 * preco_105))
  total += quant_105 * preco_105

print('Total do pedido: R$ %.2f' %total)
