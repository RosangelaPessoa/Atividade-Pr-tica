#Q6

import numpy as np

class Lista_sequencial:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.u_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  def imprimir(self):
    if self.u_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.u_posicao + 1):
        print(i, ' - ', self.valores[i])

  def inserir(self, valor):
    if self.u_posicao == self.capacidade - 1:
      print('Capacidade total atingida')
    else:
      self.u_posicao += 1 
      self.valores[self.u_posicao] = valor 

  def pesquisar(self, valor):
    for i in range(self.u_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1

  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return 1
    else:
      for i in range(posicao, self.u_posicao):
        self.valores[i] = self.valores[i + 1]
      
      self.u_posicao -= 1
