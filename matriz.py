import numpy
import random

def exibeMatriz(matriz,msg):
  if msg:
    print(msg,'\n')
  print(numpy.matrix(matriz),'\n')
  
def preencheMatriz(matriz):
  print("Preencha a matriz.")
  for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
      print('Linha',i+1,'coluna',j+1,':')
      matriz[i][j] = input()
  return matriz

def preencheAleatorio(matriz):
  for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
      matriz[i][j] =  random.randint(0, 99)
  return matriz

def inverte(matriz):
  novaMatriz = numpy.flipud(matriz)
  return novaMatriz

def rotacionar(matriz):
  #novaMatriz = numpy.zeros((len(matriz), len(matriz)),dtype=int)
  diagSecundaria = numpy.zeros((len(matriz), len(matriz)),dtype=int)
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz)):
      if(i == (len(matriz) - 1 - j)):
        diagSecundaria[i][j] = 1
      else:
        diagSecundaria[i][j] = 0
  novaMatriz = numpy.matmul(diagSecundaria,matriz)
  exibeMatriz(diagSecundaria,'Multiplicada por: ')
  return novaMatriz

def main():
    while(True):
      ordem = int(input('Insira a ordem: '))
      matriz = numpy.zeros((ordem, ordem),dtype=int)

      print('\n','Deseja preencher ou gerar valores aleatórios?','\n')
      s = int(input('Preencher [1] - Aleatório [2]\n'))

      if(s == 1):
          matriz = preencheMatriz(matriz)
      else:
          matriz = preencheAleatorio(matriz)

      exibeMatriz(matriz,'\nA matriz é: ')
      exibeMatriz(rotacionar(matriz),'O resultado é: ')

#entrypoint
main()


